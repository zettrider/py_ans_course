#!/usr/bin/env python

import telnetlib
import time

remote_conn = telnetlib.Telnet('184.105.247.70', 23, 6)
#print remote_conn.read_until('sername:', 6)
remote_conn.write('pyclass' + '\n')

#print remote_conn.read_until('word:', 6)
remote_conn.write('88newclass' + '\n')

time.sleep(1)
print remote_conn.read_very_eager()


remote_conn.write('show ip int brief' + '\n')

time.sleep(1)
print remote_conn.read_very_eager()

remote_conn.close()
