#!/usr/bin/env/python

'''
Making a Telnet Script to get show command output from cisco routeri

'''
#Making a Telnet Script to get show command output from cisco router
#Sahil Pujani

import telnetlib
import time
import socket
import sys
import getpass


TELNET_PORT = 23
TELNET_TIMEOUT = 6


class TelnetConnection(object):
    ''' Use Telnetconnection Class to assign IP_add and Password'''
    def __init__(self):
        '''This function will be used to initialise each object with the following variables'''
        self.ip_addr = raw_input("IP address: ")
        #self.ip_addr = ip_addr.strip()
        self.username = 'pyclass'
        self.password = getpass.getpass()
        self.remote_conn = ''


    def connection(self):
        '''Connection will be made to the device using this function.
        The telnet connection object will be handed over remote_conn variable'''
        try:
            self.remote_conn = telnetlib.Telnet(self.ip_addr, TELNET_PORT, TELNET_TIMEOUT)
            print "Connected"
            #return remote_conn
        except socket.timeout:
            sys.exit("Connection timed out")


    def login(self):
        '''Used to login to the device
        '''
        output = self.remote_conn.read_until("sername:", TELNET_TIMEOUT)
        self.remote_conn.write(self.username + '\n')
        output += self.remote_conn.read_until("ssword:", TELNET_TIMEOUT)
        self.remote_conn.write(self.password + '\n')
        return output


    def disable_cisco_paging(self, paging_cmd='terminal length 0'):
        '''Disable paging '''
        self.remote_conn.write(paging_cmd + '\n')
        time.sleep(1)


    def send_command(self, cmd):
        '''Used to send command '''
        cmd = cmd.rstrip()
        self.remote_conn.write(cmd + '\n')
        time.sleep(1)
        show_output = self.remote_conn.read_very_eager()
        print show_output


    def close(self):
        '''close connection to device'''
        self.remote_conn.close()
        print "Connection Closed"


def main():
    ''' Main function to orchestrate the program'''
    t_1 = TelnetConnection()
    t_1.connection()
    output = t_1.login()
    print output
    t_1.disable_cisco_paging()
    t_1.send_command('show ip int br')
    t_1.close()


if __name__ == '__main__':
    main()
