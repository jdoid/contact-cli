# find_contact

A command line program to search contact information from JSON.  JSON file is created from the input of a csv file.

## Purpose

This is a CLI application that can be used to search a JSON directory of contacts.

The JSON file does follow a certain pattern of data converted from a fixed format csv file.

## Usage

1. Get distribution file and extract - 

2. Change to 'contact' directory.

3. First time, run with csv input file location

    `python main.py -i <c:\path to\filename.csv>`
    
    * Example from Windows shell:
    `python main.py -i C:\Users\username\Documents\directory.csv`
    
    > Updating directory with new csv: C:\Users\username\Documents\directory.csv

    > Enter first or last name to search (case sensitive) :

4. Run without need to update csv file

    `python main.py`

## License

find_contact is provided under the MIT License.
