#!/usr/bin/env python

'''
Using SNMPv3 create a script that detects router configuration changes.

If the running configuration has changed, then send an email notification to
yourself identifying the router that changed and the time that it changed.

In this exercise, you will possibly need to save data to an external file. One
way you can accomplish this is by using a pickle file.
'''

import cPickle as pickle
import os.path
from getpass import getpass
from datetime import datetime

from snmp_helper import snmp_get_oid_v3, snmp_extract
from email_helper import send_mail

#Used oids
runLastChange = '1.3.6.1.4.1.9.9.43.1.1.1.0'
sysName = '1.3.6.1.2.1.1.5.0'
sysUptime = '1.3.6.1.2.1.1.3.0'

def main():

    # SNMPv3 Connection Parameters
    rtr1_ip_addr = raw_input("Enter pynet-rtr1 IP: ")
    rtr2_ip_addr = raw_input("Enter pynet-rtr2 IP: ")
    my_key = getpass(prompt="Auth + Encryption Key: ")

    a_user = 'pysnmp'
    portv3 = 161
    auth_key = my_key
    encrypt_key = my_key

    snmp_user = (a_user, auth_key, encrypt_key)
    pynet_rtr1 = (rtr1_ip_addr, portv3)
    pynet_rtr2 = (rtr2_ip_addr, portv3)

    print "test"

    for a_device in (pynet_rtr1, pynet_rtr2):
        print "test2"
        for oid in (sysName, sysUptime, runLastChange):
            print "test3"
            print snmp_extract(snmp_get_oid_v3(a_device, snmp_user, oid=oid))

if __name__ == '__main__':
    main()
