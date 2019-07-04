# Hillary Clinton Email Generator

The project is using [markovify library](https://github.com/jsvine/markovify) (Markov Chains) to generate Hillary Clinton emails (and her colleagues) based on the [email corpus that's publicly available](https://kaggle.com/kaggle/hillary-clinton-emails).

#### To generate emails
Call `python generate_emails.py <number_of_emails>`. To use additional arguments, refer to:
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

#### To regenerate the Markov model
Call `python generate_model.py`. To use additional arguments, refer to:
```
usage: generate_model.py [-h]
                         [--markov_model_state_size MARKOV_MODEL_STATE_SIZE]
                         [--use_only_hillarys_emails]
                         [--emails_path EMAILS_PATH]
                         [--content_model_path CONTENT_MODEL_PATH]
                         [--subject_model_path SUBJECT_MODEL_PATH]

optional arguments:
  -h, --help            show this help message and exit
  --markov_model_state_size MARKOV_MODEL_STATE_SIZE
                        State size of the Markov model to use. Default is 2
  --use_only_hillarys_emails
                        Include this flag to generate the model only from
                        Hillary's emails. Default is False
  --emails_path EMAILS_PATH
                        Path to load the emails from. Default is
                        /home/dio/Projects/upwork_clinton/Emails.csv
  --content_model_path CONTENT_MODEL_PATH
                        Path to load the content model from. Default is
                        /home/dio/Projects/upwork_clinton/content_model.json
  --subject_model_path SUBJECT_MODEL_PATH
                        Path to load the subject model from. Default is
                        /home/dio/Projects/upwork_clinton/subject_model.json
```