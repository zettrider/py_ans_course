#!/usr/bin/env python

snmp_oids = (
#    ('sysName', '1.3.6.1.2.1.1.5.0', None),
    ('sysUptime', '1.3.6.1.2.1.1.3.0', None),
    ('runLastChange', '1.3.6.1.4.1.9.9.43.1.1.1.0', True),
    ('runLastSave', '1.3.6.1.4.1.9.9.43.1.1.2.0', True),
    ('startLastChange', '1.3.6.1.4.1.9.9.43.1.1.3.0', True),
)

IP = '184.105.247.71'
portv3 = 161
a_user = 'pysnmp'
auth_key = 'galileo1'
encrypt_key = 'galileo1'
snmp_user = (a_user, auth_key, encrypt_key)
pynet_rtr = (IP, portv3)

import snmp_helper

sysName = snmp_helper.snmp_get_oid_v3(pynet_rtr, snmp_user, oid='1.3.6.1.2.1.1.5.0')

print snmp_helper.snmp_extract(sysName) + " - " + IP

for desc, an_oid, is_count in snmp_oids:
    snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr, snmp_user, oid=an_oid)
    output = snmp_helper.snmp_extract(snmp_data)
    print "%s    %s" % (output, desc)
