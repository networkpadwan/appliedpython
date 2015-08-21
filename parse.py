#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

print "We will use this program to parse a cisco config file"
filename = raw_input("Please enter the name of the file that needs to be parsed: ")
#print filename
input_file = CiscoConfParse(filename)
crypto = input_file.find_objects(r"^crypto map CRYPTO")

for item in crypto:
    print item.text
    for child in item.children:
        print child.text

