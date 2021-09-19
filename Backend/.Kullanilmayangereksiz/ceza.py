#!/usr/bin/python3
import ipaddress
import aiosnmp
import asyncio
import binascii
import sys
import subprocess
from routeros_api import Api
import requests


# async def GetSnmp(ip):
#         # "1.3.6.1.2.1.2.2.1.6.1", '1.3.6.1.4.1.43356.2.1.2.5.7.0',
#             async with aiosnmp.Snmp(host=ip, port=161, community="public") as snmp:
#                 # "Routerboard.com"         # Mimosa Mac Adress                # Ubiquiti Networks Inc
#                 for res in await snmp.get(".1.3.6.1.4.1.41112.1.4.5.1.5"):
#                     print(res.value)
# asyncio.run(GetSnmp('10.104.1.21'))

def SnmpCompanyName(self, ip):

    shell = subprocess.run(['snmpwalk', '-c', 'public', '-v', '1', ''+ip+'',
                            '1.3.6.1.2.1.2.2.1.6.2'], check=True, capture_output=True)
    udpPort = shell.stdout.decode()
    PureSnmp = udpPort.split(":")[1]
    return PureSnmp


async def Data():
    async with aiosnmp.Snmp(host="10.50.254.253", port=161, community="public") as snmp:
        getlist = []
        for res in await snmp.walk('1.3.6.1.2.1.2.2.1.6.2'):
            print(res.value.decode())



asyncio.run(Data())