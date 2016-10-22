#!/usr/bin/env python

'''
Write a Python program that creates a list. One of the elements of the list
should be a dictionary with at least two keys. Write this list out to a file
using both YAML and JSON formats. The YAML file should be in the expanded form.
'''

import yaml
import json

dict_asa1 = {
         'ip_addr': '10.10.10.1',
         'location': 'left of the middle',
         'responsible': 'bofh',
         'vpn': 'yes'
}

dict_asa2 = {
        'ip_addr': '10.10.11.1',
        'location': 'up and away',
        'responsible': 'packet wizard',
        'vpn': 'nope'
}

list_network = [
        'Site 1',
        '3rd floor',
        dict_asa1,
        dict_asa2,
        'PBR'
]

with open("ex6.yml", "w") as f:
    f.write(yaml.dump(list_network, default_flow_style=False))

with open("ex6.json", "w") as f:
    json.dump(list_network, f)
