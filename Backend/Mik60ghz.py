#!/usr/bin/python3
from typing import List
from Db.PoyrazLink import Poyrazdb
from routeros_api import Api
import mysql.connector
from hurry.filesize import size, alternative


class Mik60gHz:
        
        
    db= Poyrazdb()

    def Mik60ghz(self,ip):
        try:

            Apir = Api(ip, "admin", "Password")
        except Exception as err:
            return {"err": err}

        ethernet = Apir.talk("/interface/ethernet/getall")
        ipAdress = Apir.talk("/ip/address/print")
        resource = Apir.talk("/system/resource/print")
        RouterBoard = Apir.talk("/system/routerboard/getall")
        interface = Apir.talk("/interface/getall")
        wlan = Apir.talk("/interface/w60/getall")
        wlandata = Apir.talk("/interface/w60g/monitor\n=numbers=wlan60-1\n=once=")
        systemName = Apir.talk("/system/identity/getall")
        eth = Apir.talk("/interface/ethernet/monitor\n=numbers=ether1\n=once=")

        for cd in wlan:
            # wLans = cd['default-name']
            wMacAd = cd["mac-address"]
            wMode = cd["mode"]
            # wBand = cd['band']
            # wChannelWidth = cd['channel-width']
            wFrequency = cd["frequency"]
            # wscanList = cd['scan-list']
            # wtxChains = cd['tx-chains']
            # wrxChains = cd['rx-chains']
            # wProtocol = cd['wireless-protocol']
            wRunning = cd["running"]
            wDisable = cd["disabled"]

        for eth0 in eth:
            pass
        for sn in systemName:
            systemNames = sn["name"]
        for xd in ethernet:
            allEthernet = xd["default-name"]
            macAdress = xd["mac-address"]
            Running = xd["running"]
            speed = xd["speed"]
            Disable = xd["disabled"]

        for eb in RouterBoard:
            nowFirmware = eb["current-firmware"]
            seri = eb["serial-number"]
        for rr in resource:
            uptime = rr["uptime"]
            boardname = rr["board-name"]
            cpu1 = rr["cpu-load"]
        return [
            {
                # 'ActiveUser': activeUser,
                # "Ip_Addres": ipads,
                "Interface": interface,
                "Wlandata": wlandata,
                "system": [
                    {
                        "BoardName": boardname,
                        "Uptime": uptime,
                        "Serial_Number": seri,
                        "Firmware": nowFirmware,
                        "DeviceName": systemNames,
                        "Cpu": cpu1,
                    }
                ],
                "Getcurrent": self.GetcurrentData(ip=ip,Apir=Apir),
                "Ipadres": ipAdress[0]["address"][:-3],
                "Ethernet": [
                    {
                        "EthernetRate": eth0["rate"],
                        "Ethernet": allEthernet,
                        "Ethernet_Mac": macAdress,
                        "Ethernet_Running": Running,
                        "Ethernet_Speed": speed,
                        "Ethernet_Disable": Disable,
                    }
                ],
                "wireless": [
                    {
                        "Wireless_Mode": wMode,
                        "Wireless_Frequency": wFrequency,
                        "Wireless_Disable": wDisable,
                        "Wireless_MacAdress": wMacAd,
                        "Wireless_Running": wRunning,
                    }
                ],
            }
        ]


    def GetcurrentData(self,ip,Apir):
        getRequest = Apir.talk("/interface/monitor-traffic\n=interface=ether1\n=once=")
        for x in getRequest:
            Tx = size(int(x["tx-bits-per-second"]), system=alternative)
            Rx = size(int(x["rx-bits-per-second"]), system=alternative)
            # print(Tx,Rx)
            return {"Tx": Tx, "Rx": Rx}


    def Lastendpoint(self):
        Ipdata = self.db.Mikrotik60gHz_db()
        Lists = []
        for x in Ipdata:
            # print(x)
            L = self.Mik60ghz(x)
            # print(L)
            for Ls in L:
                # print(Ls)
                Lists.append(Ls)

            # Lists.append(L)

        return Lists


    print(Lastendpoint())

    # ["10.124.7.9","10.121.2.3"]
