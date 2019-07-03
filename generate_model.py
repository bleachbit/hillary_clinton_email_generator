import csv
import json
import os.path
import re
import argparse

import markovify

USE_ONLY_HILLARYS_EMAILS = False
BASE_PATH = os.path.dirname(os.path.realpath(__file__))
CONTENT_MODEL_PATH = os.path.join(BASE_PATH, 'content_model.json')
SUBJECT_MODEL_PATH = os.path.join(BASE_PATH, 'subject_model.json')
EMAILS_PATH = os.path.join(BASE_PATH, 'Emails.csv')
MARKOV_MODEL_STATE_SIZE = 2


def _get_emails(emails_path=EMAILS_PATH, field=None, use_only_hillarys_emails=USE_ONLY_HILLARYS_EMAILS):
    with open(emails_path, 'r') as emails_file:
        for email in csv.DictReader(emails_file):
            if use_only_hillarys_emails and (email['SenderPersonId'] == '80') or not use_only_hillarys_emails:  # 80 is the person ID from Persons.csv file
                if field:
                    email = email[field]
                yield email


def get_recipients():
    recipients = set()
    email_regex = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
    for email in _get_emails():
        for recipient in (email['ExtractedFrom'], email['ExtractedTo'], email['ExtractedCc'], email['MetadataFrom'], email['MetadataTo'], email['ExtractedTo']):
            recipient = recipient.replace('©', '@')  # fixes some mistakes
            result = re.search(email_regex, recipient)
            if result:
                recipients.add(result.group(0))
    return list(recipients)


def _generate_model(field, emails_path=EMAILS_PATH, retain_original=True, markov_model_state_size=MARKOV_MODEL_STATE_SIZE, use_only_hillarys_emails=USE_ONLY_HILLARYS_EMAILS, **kwargs):
    return markovify.Text(_get_emails(field=field, emails_path=emails_path, use_only_hillarys_emails=use_only_hillarys_emails), retain_original=retain_original, state_size=markov_model_state_size, **kwargs)


def _serialize_model(model, model_path):
    with open(model_path, 'w') as model_file:
        return json.dump(model.to_dict(), model_file)


def generate_models(subject_model_path=SUBJECT_MODEL_PATH, content_model_path=CONTENT_MODEL_PATH, emails_path=EMAILS_PATH, markov_model_state_size=MARKOV_MODEL_STATE_SIZE, **kwargs):
    model = _generate_model(field='ExtractedBodyText', emails_path=emails_path, markov_model_state_size=markov_model_state_size, **kwargs)
    _serialize_model(model, content_model_path)

    model = _generate_model(field='ExtractedSubject', emails_path=emails_path, markov_model_state_size=markov_model_state_size, **kwargs)
    _serialize_model(model, subject_model_path)


def _load_model(model_path):
    with open(model_path, 'r') as model_file:
        return markovify.Text.from_dict(json.load(model_file))


def load_subject_model(model_path=SUBJECT_MODEL_PATH):
    return _load_model(model_path)


def load_content_model(model_path=CONTENT_MODEL_PATH):
    return _load_model(model_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--markov_model_state_size', default=MARKOV_MODEL_STATE_SIZE, type=int, help="State size of the Markov model to use. Default is {}".format(MARKOV_MODEL_STATE_SIZE))
    parser.add_argument('--use_only_hillarys_emails', default=USE_ONLY_HILLARYS_EMAILS, action='store_true', help="Include this flag to generate the model only from Hillary's emails. Default is {}".format(USE_ONLY_HILLARYS_EMAILS))
    parser.add_argument('--emails_path', default=EMAILS_PATH, help="Path to load the emails from. Default is {}".format(EMAILS_PATH))
    parser.add_argument('--content_model_path', default=CONTENT_MODEL_PATH, help="Path to load the content model from. Default is {}".format(CONTENT_MODEL_PATH))
    parser.add_argument('--subject_model_path', default=SUBJECT_MODEL_PATH, help="Path to load the subject model from. Default is {}".format(SUBJECT_MODEL_PATH))

    args = parser.parse_args()
    generate_models(**dict(args.__dict__))
