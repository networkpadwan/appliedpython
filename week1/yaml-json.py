#!/usr/bin/env python
#Exercise 1 step 6

import yaml
import json

print "This program will write out a list to a file using both YAML and JSON format"
list1 = ['UNO', 'DOS', 3, {'a':'apple', 'b': 'ball'}]

with open("yaml-file.yml", "w") as fout:
    fout.write(yaml.dump(list1, default_flow_style = False))


with open("json-file.json", "w") as fout:
    json.dump(list1, fout)
