#!/usr/bin/python3

import nmap3
from RouteroS import routeros_api
Api = routeros_api.Api
CreateSocketError = routeros_api.CreateSocketError
LoginError = routeros_api.LoginError
nmap = nmap3.NmapHostDiscovery()
Api


class SetupMethod:

    def Initilazing(self, address, username, password):
        if self.portActive(address):
            try:
                Router = Api(address=address, user=username, password=password)
                for x in Router.talk('/ip/arp/print'):
                    if 'mac-address'  in  x:
                        self.Arp_Resolve(x)
            except (CreateSocketError, LoginError) as err:
                return "Giris Basarisiz.", str(err)

    def Arp_Resolve(self, data):
        Ip_v4 = data['address']
        Mac = data['mac-address']
        Intf = data['interface']
        print(Ip_v4,Mac,Intf)
        
    def portActive(self, Ip_adres, port="8728"):
        result = nmap.nmap_portscan_only(Ip_adres, args="-p "+port+"")
        b = result[Ip_adres]['ports']
        for cl in b:
            if cl['state'] == 'open':
                return True
    