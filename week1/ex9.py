#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse
cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

cr_pfs2 = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", 
        childspec=r"set pfs group2")

print "\nCrypto Maps using PFS group2:"
for i in cr_pfs2:
    print i.text
