# Hillary Clinton Email Generator

The project uses the [markovify library](https://github.com/jsvine/markovify) (Markov Chains) and [Hillary Clinton's public email corpus](https://kaggle.com/kaggle/hillary-clinton-emails) to generate random emails by Clinton and her colleagues.

This email generator does the reverse of what [Hillary Clinton's IT guy did to her email server using BleachBit](https://www.bleachbit.org/news/bleachbit-stifles-investigation-hillary-clinton): instead of deleting Clinton's emails, it generates them. Remarkably, both are anti-forensic techniques because generating junk makes it more difficult to find your important data. Using the generator is like adding a haystack on top of the proverbial needle: it's harder to find the needle in the haystack than to find the needle in a clean space.

This repository has only the command-line version, which requires Python 2.7 or 3.x. For a GUI version with an installer, use [BleachBit](https://www.bleachbit.org)

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
                        ./emails.txt
  --content_model_path CONTENT_MODEL_PATH
                        Path to load the content model from. Default is
                        ./content_model.json
  --subject_model_path SUBJECT_MODEL_PATH
                        Path to load the subject model from. Default is
                        ./subject_model.json
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
                        ./Emails.csv
  --content_model_path CONTENT_MODEL_PATH
                        Path to load the content model from. Default is
                        ./content_model.json
  --subject_model_path SUBJECT_MODEL_PATH
                        Path to load the subject model from. Default is
                        ./subject_model.json
```

#### Links

* [Wall Street Journal: Clinton Email Cruncher](https://github.com/wsjdata/clinton-email-cruncher)
* [benhamner/hillary-clinton-emails](https://github.com/benhamner/hillary-clinton-emails)

#### Licenses

The United States Department of State released [Hillary Clinton's emails](https://foia.state.gov/Search/Collections.aspx) into the public domain.

Markovify uses the [MIT license](https://github.com/jsvine/markovify/blob/master/LICENSE.txt).

The Hillary Clinton email generator uses the [GNU General Public License version 3](COPYING) or later.
[Dionyz Lazar](https://dionysio.com/) wrote the original version under contract.
Copyright (C) 2019 by Andrew Ziem.
