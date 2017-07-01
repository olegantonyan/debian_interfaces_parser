# -*- coding: utf-8 -*-

import unittest
import os

import debian_interfaces_parser.interfaces as interfaces


def load_fixture(name):
    return interfaces.Interfaces(os.path.dirname(os.path.realpath(__file__)) + '/' + name)


class InterfacesTest(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(len(load_fixture('interfaces1').parse_all()), 4)
        for i in load_fixture('interfaces1').parse_all():
            self.assertEqual(i.auto, True)
            if i.name == 'lo':
                self.assertEqual(i.src, 'loopback')
            elif i.name == 'eth0:0':
                self.assertEqual(i.src, 'static')
                self.assertEqual(i.address, '10.10.10.2')
                self.assertEqual(i.netmask, '255.255.255.252')
            elif i.name == 'eth0':
                self.assertEqual(i.src, 'static')
                self.assertEqual(i.address, '192.168.1.170')
                self.assertEqual(i.netmask, '255.255.255.0')
                self.assertEqual(i.gateway, '192.168.1.1')
                self.assertEqual(i.dns_nameservers, ['192.168.1.1', '8.8.8.8'])
            elif i.name == 'wlan0':
                self.assertEqual(i.src, 'dhcp')
                self.assertEqual(i.wpa_ssid, 'hello')
                self.assertEqual(i.wpa_psk, 'hello_123')

    def test_case2(self):
        self.assertEqual(len(load_fixture('interfaces2').parse_all()), 4)
        for i in load_fixture('interfaces2').parse_all():
            self.assertEqual(i.auto, True)
            if i.name == 'lo':
                self.assertEqual(i.src, 'loopback')
            elif i.name == 'eth0:0':
                self.assertEqual(i.src, 'static')
                self.assertEqual(i.address, '10.10.10.2')
                self.assertEqual(i.netmask, '255.255.255.252')
            elif i.name == 'eth0':
                self.assertEqual(i.src, 'static')
                self.assertEqual(i.address, '192.168.1.170')
                self.assertEqual(i.netmask, '255.255.255.0')
                self.assertEqual(i.gateway, '192.168.1.1')
                self.assertEqual(i.dns_nameservers, ['192.168.1.1', '8.8.8.8'])
            elif i.name == 'wlan0':
                self.assertEqual(i.src, 'dhcp')
                self.assertEqual(i.wpa_ssid, 'hello')
                self.assertEqual(i.wpa_psk, 'hello_123')

