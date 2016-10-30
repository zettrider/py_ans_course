#!/usr/bin/env python

from snmp_helper import snmp_get_oid,snmp_extract

COMMUNITY_STRING = 'galileo'
SNMP_PORT = 161
#IP='184.105.247.70'

rtr1 = ('184.105.247.70',COMMUNITY_STRING, SNMP_PORT)
rtr2 = ('184.105.247.71', COMMUNITY_STRING, SNMP_PORT)

#a_device = (IP, COMMUNITY_STRING, SNMP_PORT)

sysName_OID = '1.3.6.1.2.1.1.5.0'
sysDescr_OID = '1.3.6.1.2.1.1.1.0'

def main():

    for device in (rtr1, rtr2):
        print "\n*********************"
        for OID in (sysName_OID, sysDescr_OID):
            snmp_data = snmp_get_oid(device, oid=OID)
            output = snmp_extract(snmp_data)

            print output
        print "*********************"
    print

if __name__ == "__main__":
    main()
