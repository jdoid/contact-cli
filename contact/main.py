import sys
import getopt

def main():
    input_csv_file = ''

    # check for usage
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
                print(input_csv_file)


if __name__ == '__main__':
    main()