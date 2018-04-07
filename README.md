# contact-cli

A command line program to search contact information from JSON.

## Purpose

This is a CLI application that can be used to search a JSON directory of contacts.

The JSON file does follow a certain pattern of data converted from a fixed format csv file.

## Usage

Standalone: To run as standalone application - 

* Extract contact-cli-master.zip

* Change to root directory of the unzipped file.

* Optional: Replace data/directory.json with same named file that includes data of choice rather than test data. Include top level key "peoples".  See current directory.json.

* Run base script

    $ python run_contact.py

LIB: If you've cloned this project, and want to install as a library run - 

* Extract contact-cli-master.zip

* Change to root directory of the unzipped file.

* Run Python package manager

    $ pip install .

## License

contact-cli is provided under the MIT License.