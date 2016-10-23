#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse
cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

cr_no_aes = cisco_cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO",
                childspec=r"AES")

for i in cr_no_aes:
	print i.text
	child = i.children
	for i in child:
		if "transform-set" in i.text:
			print i.text
