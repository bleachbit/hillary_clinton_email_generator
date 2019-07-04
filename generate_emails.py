#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import email.generator
from email.mime.text import MIMEText
import os.path
import random
from datetime import datetime, timedelta

from generate_model import load_content_model, load_subject_model, BASE_PATH, CONTENT_MODEL_PATH, SUBJECT_MODEL_PATH

EMAIL_OUTPUT_PATH = os.path.join(BASE_PATH, 'emails.txt')
RECIPIENTS = ['0emillscd@state.gov', '1ilotylc@state.gov', 'abdinh@state.gov', 'abedin@state.gov', 'abedinh@state.gov', 'abendinh@state.gov', 'adedinh@state.gov', 'adlerce@state.gov', 'aliilscd@state.gov', 'baerdb@state.gov', 'baldersonkm@state.gov', 'balderstonkm@state.gov', 'bam@mikuiski.senate.gov', 'bam@mikulski.senate.gov', 'bealeca@state.gov', 'bedinh@state.gov', 'benjamin_moncrief@lemieux.senate.gov', 'blaker2@state.gov', 'brimmere@state.gov', 'brod17@clintonernail.com', 'burnswj@state.gov', 'butzgych2@state.gov', 'campbelikm@state.gov', 'carsonj@state.gov', 'cholletdh@state.gov', 'cindy.buhl@mail.house.gov', 'colemancl@state.gov', 'crowleypj@state.gov', 'danielil@state.gov', 'daniew@state.gov', 'david_garten@lautenberg.senate.gov', 'dewanll@state.gov', 'dilotylc@state.gov', 'eabedinh@state.gov', 'emillscd@state.gov', 'esullivanjj@state.gov', 'feltmanjd@state.gov', 'filotylc@state.gov', 'fuchsmh@state.gov', 'gll@state.gov', 'goldbergps@state.gov', 'goldenjr@state.gov', 'gonzalezjs@state.gov', 'gordonph@state.gov', 'h@state.gov', 'hanieymr@state.gov', 'hanleymr@state.gov', 'hanleyrnr@state.gov', 'harileymr@state.gov', 'hdr22@clintonemai1.com', 'hilicr@state.gov', 'hillcr@state.gov', 'holbrookerc@state.gov', 'hormatsrd@state.gov', 'hr15@att.blackberry.net', 'hr15@mycingular.blackberry.net', 'hrod17@c1intonemai1.com', 'huma@clintonemail.com', 'hyded@state.gov', 'ian1evqr@state.gov', 'ieltmanjd@state.gov', 'iewjj@state.gov', 'iilotylc@state.gov', 'imillscd@state.gov', 'info@mailva.evite.com', 'inh@state.gov', 'iviillscd@state.gov', 'jilotylc@state.gov', 'jj@state.gov', 'jonespw2@state.gov', 'kellyc@state.gov', 'klevorickcb@state.gov', 'kohhh@state.gov', 'kohliff@state.gov', 'laszczychj@state.gov', 'lc@state.gov', 'lewij@state.gov', 'lewjj@state.gov', 'lewn@state.gov', 'lilotylc@state.gov', 'macmanusje@state.gov', 'marshalicp@state.gov', 'marshallcp@state.gov', 'mchaleja@state.gov', 'mhcaleja@state.gov', 'millscd@state.aov', 'millscd@state.gov', 'millscd@tate.gov', 'mr@state.gov', 'muscantinel@state.gov', 'muscatinel@state.gov', 'nidestr@state.gov', 'njj@state.gov', 'nulandvi@state.gov', 'ogordonph@state.gov', 'oterom2@state.gov', 'posnermh@state.gov', 'postmaster@state.gov', 'r@state.gov', 'reines@state.gov', 'reinesp@state.gov', 'reinespi@state.gov', 'ricese@state.gov', 'rnillscd@state.gov', 'rodriguezme@state.gov', 'rooneym@state.gov', 's_specialassistants@state.gov', 'schwerindb@state.gov', 'shannonta@state.gov', 'shapiroa@state.gov', 'shermanwr@state.gov', 'slaughtera@state.gov', 'smithje@state.gov', 'steinbertjb@state.gov', 'sterntd@state.gov', 'stillivaral@state.gov', 'sullivanjj@state.gov', 'tanleyrnr@state.gov', 'tauschere0@state.gov', 'tauschereo@state.gov', 'tillemannts@state.gov', 'toivnf@state.gov', 'tommy_ross@reid.senate.gov', 'u@state.gov', 'ullivanjj@state.gov', 'vaimorou@state.gov', 'valenzuelaaa@state.gov', 'valmdrou@state.gov', 'valmmorolj@state.gov', 'valmorolj@state.gov', 'vermarr@state.gov', 'verveerms@state.gov', 'walmorou@state.gov', 'werveerms@state.gov', 'woodardew@state.gov', 'yeryeerms@state.gov']
DEFAULT_NUMBER_OF_EMAILS = 5
DEFAULT_SUBJECT_LENGTH = 64
DEFAULT_NUMBER_OF_SENTENCES = 5


def _get_random_recipient():
    return random.choice(RECIPIENTS)


def _get_random_datetime(min_year=2011, max_year=2012):
    date = datetime.strptime('{} {}'.format(random.randint(1, 365), random.randint(min_year, max_year)), '%j %Y')
    return date.strftime('%A, %B %d, %Y %I:%M %p')  # Saturday, September 15, 2012 2:20 PM


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
