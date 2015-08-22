#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

print "We will use this program to parse a cisco config file"
filename = raw_input("Please enter the name of the file that needs to be parsed: ")
#print filename
input_file = CiscoConfParse(filename)
crypto_find = input_file.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"pfs group2")
#print crypto_find
for item in crypto_find:
    print item.text
