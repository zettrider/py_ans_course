#!/usr/bin/env python

import telnetlib
import time

def open_conn():
    remote_conn = telnetlib.Telnet('184.105.247.70', 23, 6)
    #print remote_conn.read_until('sername:', 6)
    remote_conn.write('pyclass' + '\n')

    #print remote_conn.read_until('word:', 6)
    remote_conn.write('88newclass' + '\n')

    time.sleep(1)
    print remote_conn.read_very_eager()

def send_comm():
    remote_conn.write('show ip int brief' + '\n')

    time.sleep(1)
    print remote_conn.read_very_eager()

def close_conn():
    remote_conn.close()

def main():
    open_conn()
    send_comm()
    close_conn()

if __name__ == __main__
    main()
