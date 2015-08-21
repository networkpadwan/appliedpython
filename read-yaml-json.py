#!/usr/bin/env python

import json, yaml, pprint
from pprint import pprint
print "This program will read from YML and JSON files."
print "It will also pretty print the data structure that is returned from the files"

#fetching info from YML files
yml_file_name = raw_input("Please enter the YAML file name: ")
#print yml_file_name

with open(yml_file_name) as f:
    yml_list = yaml.load(f)

pprint(yml_list)
#fetching info from JSON file
json_file_name = raw_input("Please enter the JSON file name: ")
#print json_file_name
with open(json_file_name) as fout:
    json_list = json.load(fout)

pprint(json_list)


