import argparse
import email.generator
from email.mime.text import MIMEText
import os.path
import random
from datetime import datetime, timedelta

from generate_model import load_content_model, load_subject_model, BASE_PATH, CONTENT_MODEL_PATH, SUBJECT_MODEL_PATH, get_recipients

EMAIL_OUTPUT_PATH = os.path.join(BASE_PATH, 'emails.txt')
RECIPIENTS = get_recipients()
DEFAULT_NUMBER_OF_EMAILS = 5
DEFAULT_SUBJECT_LENGTH = 64
DEFAULT_NUMBER_OF_SENTENCES = 5


def _get_random_recipient():
    return random.choice(RECIPIENTS)


def _get_random_datetime(min_year=2011, max_year=2012):
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return (start + (end - start) * random.random()).strftime('%A, %B %d, %Y %I:%M %p')  # Saturday, September 15, 2012 2:20 PM


def _get_random_content(content_model, number_of_sentences=DEFAULT_NUMBER_OF_SENTENCES):
    content = []
    for _ in range(number_of_sentences):
        content.append(content_model.make_sentence())
        content.append(random.choice([' ', '\n']))
    return ''.join(content)


def _generate_email(subject_model, content_model, number_of_sentences=DEFAULT_NUMBER_OF_SENTENCES, subject_length=DEFAULT_SUBJECT_LENGTH):
    message = MIMEText(_get_random_content(content_model, number_of_sentences=number_of_sentences))

    message['Subject'] = subject_model.make_short_sentence(subject_length)
    message['To'] = _get_random_recipient()
    message['From'] = _get_random_recipient()
    message['Sent'] = _get_random_datetime()

    return message


def _generate_emails(number_of_emails, content_model_path=CONTENT_MODEL_PATH, subject_model_path=SUBJECT_MODEL_PATH,
                     number_of_sentences=DEFAULT_NUMBER_OF_EMAILS, **kwargs):
    subject_model = load_subject_model(subject_model_path)
    content_model = load_content_model(content_model_path)
    for _ in range(number_of_emails):
        yield _generate_email(subject_model, content_model, number_of_sentences=number_of_sentences)


def generate_emails(number_of_emails, content_model_path=CONTENT_MODEL_PATH, subject_model_path=SUBJECT_MODEL_PATH,
                    email_output_path=EMAIL_OUTPUT_PATH, **kwargs):
    with open(email_output_path, 'w') as email_output_file:
        email_generator = email.generator.Generator(email_output_file)
        for message in _generate_emails(number_of_emails, content_model_path, subject_model_path, **kwargs):
            email_generator.write(message.as_string())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('number_of_emails', nargs='?', default=DEFAULT_NUMBER_OF_EMAILS, type=int, help="Number of emails to generate. Default is {}".format(DEFAULT_NUMBER_OF_EMAILS))
    parser.add_argument('--number_of_sentences', default=DEFAULT_NUMBER_OF_SENTENCES, type=int, help="Number of sentences per email to generate. Default is {}".format(DEFAULT_NUMBER_OF_SENTENCES))
    parser.add_argument('--subject_length', default=DEFAULT_SUBJECT_LENGTH, type=int, help="Length of the subject line in characters. Default is {}".format(DEFAULT_SUBJECT_LENGTH))
    parser.add_argument('--email_output_path', default=EMAIL_OUTPUT_PATH, help="Path to output the generated emails to. Default is {}".format(EMAIL_OUTPUT_PATH))
    parser.add_argument('--content_model_path', default=CONTENT_MODEL_PATH, help="Path to load the content model from. Default is {}".format(CONTENT_MODEL_PATH))
    parser.add_argument('--subject_model_path', default=SUBJECT_MODEL_PATH, help="Path to load the subject model from. Default is {}".format(SUBJECT_MODEL_PATH))

    args = parser.parse_args()
    generate_emails(**dict(args.__dict__))
