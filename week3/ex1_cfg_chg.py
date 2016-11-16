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

# Constants
DEBUG = True

# 300 seconds (converted to hundredths of seconds)
RELOAD_WINDOWS = 300*100

#Used oids
RUN_LAST_CHANGED = '1.3.6.1.4.1.9.9.43.1.1.1.0'
SYS_NAME = '1.3.6.1.2.1.1.5.0'
SYS_UPTIME = '1.3.6.1.2.1.1.3.0'

def obtain_saved_objects(file_name):
    '''
    Read in previously saved objects from a pickle file

    Returns a dict:
    {
        'device_name': device_object,
        'device_name': device_object,
    }

    '''

    # Check that pickle file exists
    if not os.path.isfile(file_name):
        return {}

    # Read in any saved network devices
    net_devices = {}
    with open(file_name, 'r') as f:
        while True:
            try:
                tmp_device = pickle.load(f)
                net_devices[tmp_device.device_name] = tmp_device
            except EOFError:
                break

    return net_devices

class NetworkDevice(object):
    '''
    Simple object to store network device information

    For an alternate solution, you could replace the class/objects with
    a data structure that uses dictionaries.
    '''


    def __init__(self, device_name, uptime, last_changed, config_changed=False):
        self.device_name = device_name
        self.uptime = uptime

        # The uptime value in hundredths of seconds when running configuration
        # was last changed
        self.last_changed = last_changed
        self.run_config_changed = config_changed


def main():

    '''
    Check if the running-configuration has changed, send an email notification when
    this occurs.

    Logic for detecting the running-config has changed:

        Normal (non-reboot):

            #Did RUN_LAST_CHANGED increase
            if RUN_LAST_CHANGED > network_device_object.last_changed:
                config_changed = True

        Reboot case:

            RUN_LAST_CHANGED decreases (i.e. < network_device_object.last_changed)

            Right after reboot, RUN_LAST_CHANGED is updated upon
            load of running-config from startup-config.

            Create a grace window (RELOAD_WINDOW) for values of RUN_LAST_CHANGED.
            In other words as long as RUN_LAST_CHANGED is <= RELOAD_WINDOWS assume
            no running-config changes.

            If RUN_LAST_CHANGED is > RELOAD_WINDOW assume running-config was changed
    '''

    # Pickle file for storing previous RunningLastChanged timestamp
    net_dev_file = 'netdev.pk1'

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

    print '\n*** Checking for device changes ***'
    saved_devices = obtain_saved_objects(net_dev_file)
    print "{0} devices were previously saved\n".format(len(saved_devices))

    for a_device in (pynet_rtr1, pynet_rtr2):
        print "test2"
        for oid in (SYS_NAME, SYS_UPTIME, RUN_LAST_CHANGED):
            print "test3"
            print snmp_extract(snmp_get_oid_v3(a_device, snmp_user, oid=oid))

if __name__ == '__main__':
    main()
