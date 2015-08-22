#!/usr/bin/env/python

#Making a Telnet Script to get show command output from cisco router
#Sahil Pujani

import telnetlib
import time
import socket
import sys
import getpass


TELNET_PORT = 23
TELNET_TIMEOUT = 6


class Telnet_Connection():    
    def connection(self, ip_addr, TELNET_PORT, TELNET_TIMEOUT):
        try:
            remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
            print "Connected"
            return remote_conn
        except socket.timeout:
            sys.exit("Connection timed out")
    
    
    def login(self, username, password):
        output = self.remote_conn.read_until("sername:", TELNET_TIMEOUT)
        self.remote_conn.write(username + '\n')
        output += self.remote_conn.read_until("ssword:", TELNET_TIMEOUT)
        self.remote_conn.write(password + '\n')
        return output
    
    
    def disable_cisco_paging(self, paging_cmd ='terminal length 0'):
        self.remote_conn.write(paging_cmd + '\n')
        time.sleep(1)


    def send_command(self, cmd):
        cmd = cmd.rstrip()
        self.remote_conn.write(cmd + '\n')
        time.sleep(1)
        show_output = self.remote_conn.read_very_eager()
        print show_output

    def close(self):
        self.remote_conn.close()
        print "Connection Closed"


def main():
    ip_addr = raw_input("IP address: ")
    ip_addr = ip_addr.strip()
    username = 'pyclass'
    password = getpass.getpass()    
    username = 'pyclass'
    t1 = Telnet_Connection()
    t1.remote_conn = t1.connection(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    output = t1.login(username, password)
    print output
    t1.disable_cisco_paging()
    t1.send_command('show ip int br')
    t1.close()

if __name__ == '__main__':
    main()
