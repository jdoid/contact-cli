import sys
import getopt
from csv_to_json import CreateJson
import search_name as search

def main():
    input_csv_file = ''

    # check for command line option of new csv file
    total_args = len(sys.argv)

    if total_args > 1:
        try:
            myopts, args = getopt.getopt(sys.argv[1:],"i:")
        except getopt.GetoptError as e:
            print (str(e))
            print("Usage: %s -i <input>" % sys.argv[0])
            sys.exit(2)
        
        for o, a in myopts:
            if o == '-i':
                input_csv_file=a
                #print(input_csv_file)

    if input_csv_file:
        new_directory = CreateJson(input_csv_file)
        new_directory.create_json()


if __name__ == '__main__':
    main()
    search.main()