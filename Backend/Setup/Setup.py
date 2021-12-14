#!/usr/bin/python3
from re import A
import nmap3
from RouteroS.routeros_api import Api, CreateSocketError, LoginError
from Models.Getmac import Classmac
nmap = nmap3.NmapHostDiscovery()
class_mac = Classmac()


class SetupMethod:

    def Initilazing(self, address, username, password):
        if self.portActive(address):
            try:
                Router = Api(address=address, user=username, password=password)
                for x in Router.talk('/ip/arp/print'):
                    if 'mac-address' in x:
                        self.Arp_Resolve(x, address, username, password)
            except (CreateSocketError, LoginError) as err:
                print(err)
                return "Giris Basarisiz.", str(err)

    def Arp_Resolve(self, data, address, username, password):
        Ip_v4 = data['address']
        Mac = data['mac-address'][0:8]
        Intf = data['interface']
        result = class_mac.getMac(Mac)
        if result == "Routerboard.com":
            if self.Mikrotikdb(address, username, password) == "ap-bridge":
                # Burasi multi point yani acces point
                pass
            elif self.Mikrotikdb(address, username, password)  == 'bridge':
                # Burasi Link cihazi
                pass
            elif self.Mikrotikdb(address,username,password) == "station-bridge":
                # burasida client cihazidir
                
            
        Results = []
        
        Results.append({"ip_v4": Ip_v4, "result": result, "interface": Intf})

    def portActive(self, Ip_adres, port="8728"):
        result = nmap.nmap_portscan_only(Ip_adres, args="-p "+port+"")
        b = result[Ip_adres]['ports']
        for cl in b:
            if cl['state'] == 'open':
                return True
            
    def Mikrotikdb(self, address, username, password):
        Apiverbos = Api( address, username, password)
        Lenghtlist = Apiverbos.talk('/interface/wireless/print')
        if len(Lenghtlist) > 0:
            self.Accesspoint(Apiverbos)
            # Ozaman burasi bir Apdir veya linkdir. buradaki ayrimi yapmak icin farkli bir method olusturmam gerekiyor.
        else:
            # Ozaman burasi bir Routerdir.
            pass
        
    def Accesspoint(self,Apiverbos):
        wint = Apiverbos.talk("/interface/wireless/print")
        for x in wint:
            return x["mode"]
        