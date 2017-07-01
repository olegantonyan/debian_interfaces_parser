# -*- coding: utf-8 -*-


class Iface(object):
    def __init__(self, name, src):
        self.src = src  # static or dhcp
        self.name = name
        self.netmask = None
        self.gateway = None
        self.dns_nameservers = []
        self.address = None
        self.wpa_ssid = None
        self.wpa_psk = None
        self.auto = False

    def dump(self):
        result = ''
        if self.auto:
            result += "auto {name}\n".format(name=self.name)
        result += "iface {name} inet {src}\n".format(name=self.name, src=self.src)

        if self.wpa_ssid and self.wpa_psk:
            result += "  wpa-ssid {s}\n".format(s=self.wpa_ssid)
            result += "  wpa-psk {s}\n".format(s=self.wpa_psk)

        if self.src == 'dhcp' or self.src == 'loopback':
            return result

        if not self.address:
            raise RuntimeError('static interface must have address')
        if not self.netmask:
            raise RuntimeError('static interface must have netmask')

        result += "  address {s}\n".format(s=self.address)
        result += "  netmask {s}\n".format(s=self.netmask)

        if self.gateway:
            result += "  gateway {s}\n".format(s=self.gateway)

        if len(self.dns_nameservers) > 0:
            result += "  dns-nameservers {s}\n".format(s=', '.join(self.dns_nameservers))

        return result




