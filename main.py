# -*- coding: utf-8 -*-

import debian_interfaces_parser.interfaces as interfaces


def main():
    i = interfaces.Interfaces('/home/oleg/Desktop/interfaces')
    ifaces = i.parse_all()
    for j in ifaces:
        print(j.dump())

if __name__ == '__main__':
    main()