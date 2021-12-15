#!/usr/bin/python3
import aiosnmp
import asyncio
import subprocess
from aiosnmp.exceptions import SnmpTimeoutError
from aiosnmp.message import SnmpVersion

import requests
from Db.PoyrazLink import Poyrazdb
from routeros_api import Api
import mysql.connector
from ubntapi import Ubntos
import binascii
import os

class SnmpSignal:
    Pn = Poyrazdb()
    async def SnmpMimosa(self, ip):
        try:
            degerler = []
            async with aiosnmp.Snmp(host=ip, version=SnmpVersion.v1) as snmp:
                for res in await snmp.get(
                    [
                        "1.3.6.1.4.1.43356.2.1.2.1.1.0",
                        "1.3.6.1.4.1.43356.2.1.2.6.1.1.3.1",
                        "1.3.6.1.4.1.43356.2.1.2.6.1.1.3.2",
                    ]
                ):
                    degerler.append(res.value)
            return degerler
        except Exception as err:
            return err

    async def SnmpMikrotik(self, ip):
        """
        Bu Fonksiyonun yaptigi islem snmp ile bilgileri alip cozumleme yapiyor.
        """
        try:
            sa = Api(ip, "admin", self.linkpwd)
        except Exception as Err:
            print(Err, "Giris Kismindaki Hata")
        sa.talk("/snmp/set\n=enabled=yes")

        routermodel = sa.talk("/system/routerboard/print")[0]
        if routermodel["model"] == "RBLHGG-60ad":
            return sa.talk("/interface/w60g/monitor\n=numbers=wlan60-1\n=once=")[0]["rssi"]
        Tx_ChainsZero = sa.talk(
            "/interface/wireless/registration-table/print\n=.proplist=signal-strength-ch0.oid"
        )
        Tx_ChainsOne = sa.talk(
            "/interface/wireless/registration-table/print\n=.proplist=signal-strength-ch1.oid"
        )

        for x in Tx_ChainsZero:
            signal0 = x["signal-strength-ch0.oid"]
        for xs in Tx_ChainsOne:
            signal1 = xs["signal-strength-ch1.oid"]

        self.degerler = []
        async with aiosnmp.Snmp(
            host=ip, port=161, community="public", version=SnmpVersion.v1
        ) as snmp:
            for res in await snmp.get([signal0, signal1]):
                self.degerler.append(str(res.value))
        return self.degerler

    def SnmpUbnt(self, ip):
        ubnt = Ubntos()
        Data = ubnt.RSession(ip)
        return Data["Data"]['Data1']['wireless']["sta"][0]['signal']

    async def SnmpCompanyName(self, ip) -> str:
        async with aiosnmp.Snmp(host=ip,port=161,community="public",) as snmp:
            try:
                for res in await snmp.get([".1.3.6.1.2.1.2.2.1.6.2"]):
                    return self.MacAdresFind(binascii.hexlify(res.value).decode()[0:6].upper())

            except SnmpTimeoutError:
                #The Ubuqiti Network is returning the SnmpTimeoutError error "No Response" on the device
                shell = subprocess.run(["snmpwalk",
                        "-c",
                        "public",
                        "-v",
                        "1",
                        "" + ip + "",
                        ".1.3.6.1.2.1.2.2.1.6.2",
                    ],
                    check=True,
                    capture_output=True,
                )
                Ubuquiti = shell.stdout.decode()
                return self.Pn.MacAdresFind(Ubuquiti.split("=")[1].split("G")[1].replace(" ","").replace("\n","").replace(":","")[0:6].upper())
               

    def Lstenpoint(self, ip):
        Company = asyncio.run(self.SnmpCompanyName(ip))

        if "Ubiquiti Networks Inc." == Company:
            return self.SnmpUbnt(ip)
        elif "Mimosa Networks" == Company:
            AsyncMimosa = asyncio.run(self.SnmpMimosa(ip))
            print(AsyncMimosa)
            Asynm = str(AsyncMimosa[1])[1:3]
            return [Asynm]
        elif "Routerboard.com" == Company:
            return asyncio.run(self.SnmpMikrotik(ip))
        else:
            return "Vendor is not defined"


[
    # Ubiquiti Networks Inc
    # "Routerboard.com"
    # Mimosa Networks"
]
Obj = SnmpSignal()

Dot1 = Obj.Lstenpoint("10.104.1.21")
print(Dot1)
