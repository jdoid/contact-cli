import csv
import json
import os

class CreateJson(object):
    def __init__(self, file):
        self.csv_file = file

    def create_json(self):
        # csvfile = './directory.csv'
        print("Updating directory with new csv: " + self.csv_file)
        print()
        directory = os.path.splitext(self.csv_file)[0]
        jsonfile = '../data/directory.json'

        with open(directory + '.csv') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        # create json file.   TODO: need to clean up how to write main key (people) to file
        json_file_write = open(jsonfile, 'w')
        json_file_write.write('{\n "people"  :')

        json.dump(
            rows,
            json_file_write,
            indent = 2    
        )

        json_file_write.write('\n}')   
        json_file_write.close()