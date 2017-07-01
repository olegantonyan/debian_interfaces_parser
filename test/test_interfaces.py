# -*- coding: utf-8 -*-

import unittest
import os

import debian_interfaces_parser.interfaces as interfaces


class InterfacesTest(unittest.TestCase):
    def setUp(self):
        self.interfaces = interfaces.Interfaces(os.path.dirname(os.path.realpath(__file__)) + '/interfaces1').parse_all()

    def test(self):
        self.assertEqual(len(self.interfaces), 4)


if __name__ == '__main__':
    unittest.main()
