import csv
import json
import os


def main():
    csvfile = './directory.csv'
    directory = os.path.splitext(csvfile)[0]
    jsonfile = directory + '.json'

    with open(directory + '.csv') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # print(rows)

    json_file_write = open(jsonfile, 'w')

    json.dump(
        rows,
        json_file_write,
        indent = 2    
    )   

    json_file_write.close()

if __name__ == '__main__':
    main()