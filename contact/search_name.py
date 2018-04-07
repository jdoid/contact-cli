import json

contact_directory = "data/directory.json"

def prompt():
    name = input('Enter first or last name to search (case sensitive) : ')
    return name

def main():
    last_name = "Last Name"
    first_name = "First Name"

    person = prompt()

    with open(contact_directory) as f:
        data = json.load(f)

    f.close()

    # get full dictionary for all last name in var person
    name = [item for item in data["peoples"]
        if item[last_name] == person ]
    
    # or check for person in the first name field
    if not name:
        name = [item for item in data["peoples"]
            if person in item[first_name] ]

    # print list as there may be multiple matches
    for entry in name:
        print()
        for k,v in entry.items():
            print(k, ': \t', v)
        print()

if __name__ == '__main__':
    main()




















