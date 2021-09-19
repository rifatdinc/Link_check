#!/usr/bin/python3

from re import VERBOSE
from routeros_api import Api, CreateSocketError
import mysql.connector
from hurry.filesize import size, alternative
import json
import os
import asyncio


class Mikrotik():

    async def FirstApi(self, ip):
        try:

            self.Apir = Api(ip, "admin", '400HM14293')
        except Exception as err:
            print('asdkas=-----------------', err)
            print(self.Apir.is_alive())

            return {}
        

        ethernet = self.Apir.talk('/interface/ethernet/getall')
        self.wlan = self.Apir.talk('/interface/wireless/getall')
        self.ipAdress = self.Apir.talk('/ip/address/print')
        resource = self.Apir.talk('/system/resource/print')
        RouterBoard = self.Apir.talk('/system/routerboard/getall')
        interface = self.Apir.talk('/interface/getall')
        self.ApR = self.Apir.talk(
            '/interface/wireless/registration-table/print')

        print('s---------------------------------------------------')
        for css in self.ApR:
            self.Aprs = css['radio-name']

            self.sinyal1 = css['signal-strength-ch0']
            self.sinyal2 = css['signal-strength-ch1']
            self.sinyal3 = css['tx-signal-strength-ch0']
            self.sinyal4 = css['tx-signal-strength-ch1']
        systemName = self.Apir.talk('/system/identity/getall')
        self.eth = self.Apir.talk(
            '/interface/ethernet/monitor\n=numbers=ether1\n=once=')
        # self.activeUser = self.Apir.talk('/user/active/getall')
        # for inx in self.ipAdress:
        #     if inx['interface'] == "pppoe-out1":
        #         self.addressip = inx['address']
        #         self.ipads = self.addressip[:-3]
        for eth0 in self.eth:
            pass
        for sn in systemName:
            self.systemNames = sn['name']
        for xd in ethernet:
            self.allEthernet = xd['default-name']
            self.macAdress = xd['mac-address']
            self.Running = xd['running']
            self.speed = xd['speed']
            self.Disable = xd['disabled']
        for cd in self.wlan:
            self.wLans = cd['default-name']
            self.wMacAd = cd['mac-address']
            self.wMode = cd['mode']
            self.wBand = cd['band']
            self.wChannelWidth = cd['channel-width']
            self.wFrequency = cd['frequency']
            self.wscanList = cd['scan-list']
            self.wtxChains = cd['tx-chains']
            self.wrxChains = cd['rx-chains']
            self.wProtocol = cd['wireless-protocol']
            self.wRunning = cd['running']
            self.wDisable = cd['disabled']

        for eb in RouterBoard:
            self.nowFirmware = eb['current-firmware']
            self.seri = eb['serial-number']
        for rr in resource:
            self.uptime = rr['uptime']
            self.boardname = rr['board-name']
            self.cpu1 = rr['cpu-load']

        return [{
            # 'ActiveUser': self.activeUser,
            # "Ip_Addres": self.ipads,
            "Interface": interface,

            'system': [{
                'BoardName': self.boardname,
                'Uptime': self.uptime,
                'Serial_Number': self.seri,
                'Firmware': self.nowFirmware,
                'DeviceName': self.systemNames,
                'Cpu': self.cpu1,
            }],
            "Getcurrent": self.GetcurrentData(ip=ip),
            'Ipadres': self.ipAdress[0]['address'][:-3],

            'Ethernet': [{
                "EthernetRate": eth0['rate'],
                'Ethernet': self.allEthernet,
                'Ethernet_Mac': self.macAdress,
                'Ethernet_Running': self.Running,
                'Ethernet_Speed': self.speed,
                'Ethernet_Disable': self.Disable}],
            'wireless': [{
                'Wireless_Regestrin': self.Aprs,
                'Wireless_Mode': self.wMode,
                'Wireless_Band': self.wBand,
                'Wireless_Channel': self.wChannelWidth,
                'Wireless_Frequency': self.wFrequency,
                'Wireless_wscanList': self.wscanList,
                'Wireless_Protocol': self.wProtocol,
                'Wireless_Disable': self.wDisable,
                'Wireless_MacAdress': self.wMacAd,
                'Wireless_TxChains': self.wtxChains,
                'Wireless_Running': self.wRunning,
                'Signal': {
                    "Signal1": self.sinyal1,
                    "Signal2": self.sinyal2,
                    "Signal3": self.sinyal3,
                    "Signal4": self.sinyal4

                },
                'Wireless_RxChains': self.wrxChains}]
        }]

    def GetcurrentData(self, ip):
        Data = Api(ip, 'admin', '400HM14293')
        # print()
        getRequest = Data.talk(
            '/interface/monitor-traffic\n=interface=wlan1\n=once=')
        for x in getRequest:
            Tx = size(int(x['tx-bits-per-second']), system=alternative)
            Rx = size(int(x['rx-bits-per-second']), system=alternative)
            # print(Tx,Rx)
            return {"Tx": Tx, "Rx": Rx}
            # return{}

    def Databaseqets(self, Qstring, queryStriq):
        connection = mysql.connector.connect(host="192.168.192.2", user="root", password="As081316",
                                             database="PoyrazwifiVerici", auth_plugin='mysql_native_password')
        cursor = connection.cursor()
        cursor.execute(
            'Select distinct device,nas,ip From tblLink WHERE device="'+Qstring+'" and nas="'+queryStriq+'"  and not type="RBLHGG-60ad" ORDER BY ip')
        gels = cursor.fetchall()
        lsa = []
        for xd in gels:
            print(xd)
            qet = xd[2].decode()
            if qet not in lsa:

                lsa.append(qet.replace(" ", ""))
        return lsa

    async def LastFunc(self, Qstrinq, querySrinq):

        cv = []
        for ld in self.Databaseqets(Qstrinq, querySrinq):
            ds = asyncio.ensure_future(self.FirstApi(ld))
            cv.append(ds)
        task1 = await asyncio.gather(*cv)
        print(task1)
      

        # Apis = self.FirstApi()


m = Mikrotik()
# # print(m.qets())
# # m.Getcur
print(asyncio.run(m.LastFunc('mikrotik','Balturk5')))
