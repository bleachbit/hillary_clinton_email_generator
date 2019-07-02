import csv
import json
import os.path
import re

import markovify

USE_ONLY_HILLARY_EMAILS = True
BASE_PATH = os.path.dirname(os.path.realpath(__file__))
CONTENT_MODEL_PATH = os.path.join(BASE_PATH, 'content_model.json')
SUBJECT_MODEL_PATH = os.path.join(BASE_PATH, 'subject_model.json')
EMAILS_PATH = os.path.join(BASE_PATH, 'Emails.csv')
MARKOV_MODEL_STATE_SIZE = 2


def _get_emails(emails_path=EMAILS_PATH, field=None, use_only_hillary_email=USE_ONLY_HILLARY_EMAILS):
    with open(emails_path, 'r') as emails_file:
        for email in csv.DictReader(emails_file):
            if use_only_hillary_email and (email['SenderPersonId'] == '80') or not use_only_hillary_email:  # 80 is the person ID from Persons.csv file
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


def _generate_model(field, emails_path=EMAILS_PATH, retain_original=True, state_size=MARKOV_MODEL_STATE_SIZE, **kwargs):
    return markovify.Text(_get_emails(field=field, emails_path=emails_path), retain_original=retain_original, state_size=state_size, **kwargs)


def _serialize_model(model, model_path):
    with open(model_path, 'w') as model_file:
        return json.dump(model.to_dict(), model_file)


def generate_models(subject_model_path=SUBJECT_MODEL_PATH, content_model_path=CONTENT_MODEL_PATH, emails_path=EMAILS_PATH, **kwargs):
    model = _generate_model(field='ExtractedBodyText', emails_path=emails_path, **kwargs)
    _serialize_model(model, content_model_path)

    model = _generate_model(field='ExtractedSubject', emails_path=emails_path, **kwargs)
    _serialize_model(model, subject_model_path)


def _load_model(model_path):
    with open(model_path, 'r') as model_file:
        return markovify.Text.from_dict(json.load(model_file))


def load_subject_model(model_path=SUBJECT_MODEL_PATH):
    return _load_model(model_path)


def load_content_model(model_path=CONTENT_MODEL_PATH):
    return _load_model(model_path)


if __name__ == '__main__':
    generate_models()
