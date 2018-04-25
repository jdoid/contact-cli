import csv
import json
import os



class CreateJson(object):
    def __init__(self, file):
        self.csv_file = file

    def create_json(self):
        # csvfile = './directory.csv'
        directory = os.path.splitext(self.csv_file)[0]
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