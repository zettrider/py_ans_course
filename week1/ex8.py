#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse
cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

cry_map = cisco_cfg.find_objects(r"^crypto map CRYPTO")

for cr in cry_map:
    print cr.text
    for child in cr.children:
        print child.text
