# Hillary Clinton Email Generator

The project is using [markovify library](https://github.com/jsvine/markovify) (Markov Chains) to generate Hillary Clinton emails (and her colleagues) based on the email corpus that's publicly available.

## Usage
1. `git clone https://github.com/dionysio/hillary_clinton_email_generator`
2. Install dependencies `pip install -r requirements.txt`
3. Call `python generate_emails.py <number_of_emails>`. To use additional arguments, refer to:
```
usage: generate_emails.py [-h] [--number_of_sentences NUMBER_OF_SENTENCES]
                          [--subject_length SUBJECT_LENGTH]
                          [--email_output_path EMAIL_OUTPUT_PATH]
                          [--content_model_path CONTENT_MODEL_PATH]
                          [--subject_model_path SUBJECT_MODEL_PATH]
                          [number_of_emails]

positional arguments:
  number_of_emails      Number of emails to generate. Default is 5

optional arguments:
  -h, --help            show this help message and exit
  --number_of_sentences NUMBER_OF_SENTENCES
                        Number of sentences per email to generate. Default is
                        5
  --subject_length SUBJECT_LENGTH
                        Length of the subject line in characters. Default is
                        64
  --email_output_path EMAIL_OUTPUT_PATH
                        Path to output the generated emails to. Default is
                        /home/dio/Projects/upwork_clinton/emails.txt
  --content_model_path CONTENT_MODEL_PATH
                        Path to load the content model from. Default is
                        /home/dio/Projects/upwork_clinton/content_model.json
  --subject_model_path SUBJECT_MODEL_PATH
                        Path to load the subject model from. Default is
                        /home/dio/Projects/upwork_clinton/subject_model.json
```