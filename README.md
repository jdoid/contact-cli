# find_contact

A command line program to search contact information from JSON.  JSON file is created from the input of a csv file.

## Purpose

This is a CLI application that can be used to search a JSON directory of contacts.

The JSON file does follow a certain pattern of data converted from a fixed format csv file.

## Usage

* Get distribution file and extract - 

* Change to 'contact' directory.

* First time, run with csv input file location

    $ python run_contact.py -i <c:\path to\filename.csv>
    
    Example from Windows shell: 
    \dist\contacts_cli-0.2.0\contact> python .\run_contact.py -i C:\Users\username\Documents\directory.csv
    Updating directory with new csv: C:\Users\deank\Documents\SCC_2018_Spring_Directory.csv

    Enter first or last name to search (case sensitive) :

* Run without need to update csv file

    $ python run_contact.py

## License

contact-cli is provided under the MIT License.
