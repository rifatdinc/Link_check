#!/usr/bin/python3

from re import VERBOSE
from routeros_api import Api, CreateSocketError, RouterOSTrapError
import mysql.connector
from hurry.filesize import size, alternative
import json
import os
import asyncio
from concurrent.futures import ThreadPoolExecutor
import nmap3
from concurrent.futures import ProcessPoolExecutor
from Db.PoyrazLink import Poyrazdb


class Mikrotik:
    def __init__(self) -> None:
        self.linpaswd = os.environ.get("linpaswd")

    Pndb = Poyrazdb()

    def FirstApi(self, ip):
        try:
            self.Apir = Api(ip, "admin", "400HM14293")
        except Exception as err:
            print("Expection Login error------", err)

        interface = self.Apir.talk("/interface/getall")

        for l in interface:
            # iki ayri degisken yerine tek degiken olusturup interface isimleri
            # ve durumlarini aldim.
            w = l["default-name"]
            c = l["running"]

            if c == "false":
                print(w, "Interface Kapali")
                return {"Wlan_Kapali": True}
            else:

                ethernet = self.Apir.talk("/interface/ethernet/getall")
                self.wlan = self.Apir.talk("/interface/wireless/getall")
                self.ipAdress = self.Apir.talk("/ip/address/print")
                resource = self.Apir.talk("/system/resource/print")
                RouterBoard = self.Apir.talk("/system/routerboard/getall")

                self.ApR = self.Apir.talk(
                    "/interface/wireless/registration-table/print"
                )

                systemName = self.Apir.talk("/system/identity/getall")
                self.eth = self.Apir.talk(
                    "/interface/ethernet/monitor\n=numbers=ether1\n=once="
                )

                # print('s----------------')
                if len(self.ApR) > 0:
                    for css in self.ApR:
                        self.Aprs = css["radio-name"]

                        self.sinyal1 = css["signal-strength-ch0"]
                        self.sinyal2 = css["signal-strength-ch1"]
                        self.sinyal3 = css["tx-signal-strength-ch0"]
                        self.sinyal4 = css["tx-signal-strength-ch1"]

                else:
                    # Gelen Degerler Bos ise ikincil degerlere Bos olarak atandi
                    self.sinyal1 = "Data Boş"
                    self.sinyal2 = "Data Boş"
                    self.sinyal3 = "Data Boş"
                    self.sinyal4 = "Data Boş"

                # self.activeUser = self.Apir.talk('/user/active/getall')
                # for inx in self.ipAdress:
                #     if inx['interface'] == "pppoe-out1":
                #         self.addressip = inx['address']
                #         self.ipads = self.addressip[:-3]
                for eth0 in self.eth:
                    pass
                for sn in systemName:
                    self.systemNames = sn["name"]
                for xd in ethernet:
                    self.allEthernet = xd["default-name"]
                    self.macAdress = xd["mac-address"]
                    self.Running = xd["running"]
                    self.speed = xd["speed"]
                    self.Disable = xd["disabled"]
                if len(self.wlan) > 0:

                    for cd in self.wlan:
                        self.wLans = cd["default-name"]
                        self.wMacAd = cd["mac-address"]
                        self.wMode = cd["mode"]
                        self.wBand = cd["band"]
                        self.wChannelWidth = cd["channel-width"]
                        self.wFrequency = cd["frequency"]
                        self.wscanList = cd["scan-list"]
                        self.wtxChains = cd["tx-chains"]
                        self.wrxChains = cd["rx-chains"]
                        self.wProtocol = cd["wireless-protocol"]
                        self.wRunning = cd["running"]
                        self.wDisable = cd["disabled"]
                else:
                    self.wLans = "Data yok !!"
                    self.wMacAd = "Data yok !!"
                    self.wMode = "Data yok !!"
                    self.wBand = "Data yok !!"
                    self.wChannelWidth = "Data yok !!"
                    self.wFrequency = "Data yok !!"
                    self.wscanList = "Data yok !!"
                    self.wtxChains = "Data yok !!"
                    self.wrxChains = "Data yok !!"
                    self.wProtocol = "Data yok !!"
                    self.wRunning = "Data yok !!"
                    self.wDisable = "Data yok !!"
                for eb in RouterBoard:
                    self.nowFirmware = eb["current-firmware"]
                    self.seri = eb["serial-number"]
                for rr in resource:
                    self.uptime = rr["uptime"]
                    self.boardname = rr["board-name"]
                    self.cpu1 = rr["cpu-load"]

                return {
                    # 'ActiveUser': self.activeUser,
                    # "Ip_Addres": self.ipads,
                    "Interface": interface,
                    "system": [
                        {
                            "BoardName": self.boardname,
                            "Uptime": self.uptime,
                            "Serial_Number": self.seri,
                            "Firmware": self.nowFirmware,
                            "DeviceName": self.systemNames,
                            "Cpu": self.cpu1,
                        }
                    ],
                    "Getcurrent": self.GetcurrentData(self.Apir),
                    "Ipadres": self.ipAdress[0]["address"][:-3],
                    "Ethernet": [
                        {
                            "EthernetRate": eth0["rate"],
                            "Ethernet": self.allEthernet,
                            "Ethernet_Mac": self.macAdress,
                            "Ethernet_Running": self.Running,
                            "Ethernet_Speed": self.speed,
                            "Ethernet_Disable": self.Disable,
                        }
                    ],
                    "wireless": [
                        {
                            # 'Wireless_Regestrin': self.Aprs,
                            "Wireless_Mode": self.wMode,
                            "Wireless_Band": self.wBand,
                            "Wireless_Channel": self.wChannelWidth,
                            "Wireless_Frequency": self.wFrequency,
                            "Wireless_wscanList": self.wscanList,
                            "Wireless_Protocol": self.wProtocol,
                            "Wireless_Disable": self.wDisable,
                            "Wireless_MacAdress": self.wMacAd,
                            "Wireless_TxChains": self.wtxChains,
                            "Wireless_Running": self.wRunning,
                            "Signal": {
                                "Signal1": self.sinyal1
                                if len(self.ApR) > 0
                                else "Data Boş",
                                "Signal2": self.sinyal2
                                if len(self.ApR) > 0
                                else "Data Boş",
                                "Signal3": self.sinyal3
                                if len(self.ApR) > 0
                                else "Data Boş",
                                "Signal4": self.sinyal4
                                if len(self.ApR) > 0
                                else "Data Boş",
                            },
                            "Wireless_RxChains": self.wrxChains,
                        }
                    ],
                }

    def GetcurrentData(self, Apir):
        try:
            getRequest = Apir.talk(
                "/interface/monitor-traffic\n=interface=wlan1\n=once="
            )
        except RouterOSTrapError as r:
            return {"Tx": "Data yok", "Rx": "Data yok"}

        for x in getRequest:
            Tx = size(int(x["tx-bits-per-second"]), system=alternative)
            Rx = size(int(x["rx-bits-per-second"]), system=alternative)
            return {"Tx": Tx, "Rx": Rx}

    def MikrotikApiCheck(self, ip):
        nmap = nmap3.NmapHostDiscovery()

        results = nmap.nmap_portscan_only(ip, args="-p 8728")
        return results[ip]["ports"][0]["state"]

    def LastFunc(self, Qstrinq, querySrinq):
        kls = []
        with ProcessPoolExecutor() as executor:
            result = executor.map(
                self.FirstApi, self.Pndb.Mikrotik5gHz_db(Qstrinq, querySrinq)
            )
            print(result)
            for x in result:
                kls.append(x)
        print(kls)
        return kls
