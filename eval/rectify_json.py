#code to print the json structure of our dataset

import json
input_file = 'dev.json'
with open(input_file, "r", encoding='utf-8') as reader:
    input_data = json.load(reader)["data"]
    #print(input_data['version'])

from pprint import pprint
pprint(input_data[0])
