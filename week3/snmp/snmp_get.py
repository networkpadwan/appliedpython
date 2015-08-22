#!/usr/bin/env/python
#Program to get sys desc and sys Name from both rtr1 and rtr2


from snmp_helper import snmp_get_oid, snmp_extract


def main():

    snmp_oids = (
                ('sysDesc', '1.3.6.1.2.1.1.1.0'),
                ('sysName', '1.3.6.1.2.1.1.5.0'),
                )
    pynet_rtr1 = ('50.76.53.27', 'galileo', 7961)
    pynet_rtr2 = ('50.76.53.27', 'galileo', 8061)

    #list_device = [pynet_rtr1, pynet_rtr2]
    dict_device = {'pynet_rtr1':pynet_rtr1, 'pynet_rtr2':pynet_rtr2}
    #print type(snmp_oids)
    print '\n'
    for key in dict_device:
        device = dict_device.get(key)
        print "#"*10
        print "OUTPUT for: "+ key
        print "#"*10
        for des, oid in snmp_oids:
            snmp_data = snmp_get_oid(device, oid)
            output = snmp_extract(snmp_data)
            print des + ":  " + output
        print '\n'


if __name__ == '__main__':
    main()
