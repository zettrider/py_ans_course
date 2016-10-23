#!/usr/bin/env python
'''
Write a Python program that reads both the YAML file and the JSON file created
in exercise6 and pretty prints the data structure that is returned.
'''

import yaml
import json

from pprint import pprint

def output_format(my_list, my_str):
    '''
    Make the output format easier to read
    '''

    print '\n\n'
    print '#' * 3
    print '#' * 3 + my_str
    print '#' * 3
    pprint(my_list)

def main():
    '''
    read YAML and JSON files. Pretty print to standard out
    '''

    yaml_file = 'ex6.yml'
    json_file = 'ex6.json'

    with open(yaml_file) as f:
        yaml_list = yaml.load(f)

    with open(json_file) as f:
        json_list = json.load(f)

    output_format(yaml_list, ' YAML ')
    output_format(json_list, ' JSON')
    print '\n'

#    pprint(yaml_list)
#    pprint(json_list)

if __name__ == "__main__":
    main()
