#!/usr/bin/python3
import aiosnmp
import asyncio
import subprocess
from routeros_api import Api
import requests
import mysql.connector

class SnmpSignal():

    async def SnmpMimosa(self, ip):
        try:
            degerler = []
            async with aiosnmp.Snmp(host=ip, port=161, community="public") as snmp:

                for res in await snmp.get(['1.3.6.1.4.1.43356.2.1.2.1.1.0',
                                           '1.3.6.1.4.1.43356.2.1.2.6.1.1.3.1',
                                           '1.3.6.1.4.1.43356.2.1.2.6.1.1.3.2',
                                           ]):
                    degerler.append(res.value)
            return degerler
        except Exception as err:
            print(err)

    async def SnmpMikrotik(self, ip):
        """
        Bu Fonksiyonun yaptigi islem snmp ile bilgileri alip cozumleme yapiyor.
        """
        ip = ip
        try:

            sa = Api(ip, 'admin', '400HM14293')
        except Exception as Err:
            print(Err, "Giris Kismindaki Hata")
        sa.talk('/snmp/set\n=enabled=yes')
        Tx_ChainsZero = sa.talk(
            '/interface/wireless/registration-table/print\n=.proplist=signal-strength-ch0.oid')
        Tx_ChainsOne = sa.talk(
            '/interface/wireless/registration-table/print\n=.proplist=signal-strength-ch1.oid')

        for x in Tx_ChainsZero:
            signal0 = (x['signal-strength-ch0.oid'])
        for xs in Tx_ChainsOne:
            signal1 = (xs['signal-strength-ch1.oid'])

        self.degerler = []
        async with aiosnmp.Snmp(host=ip, port=161, community="public") as snmp:
            for res in await snmp.get([signal0, signal1]):
                self.degerler.append(str(res.value))
        return self.degerler

    def SnmpUbnt(self, ip):
        shell = subprocess.run(['snmpwalk', '-c', 'public', '-v', '1', ''+ip+'',
                               '.1.3.6.1.4.1.41112.1.4.5.1.5'], check=True, capture_output=True)
        Ubuquiti = shell.stdout.decode()
        DataUbnt = Ubuquiti.split(":")[1][2:4]
        return [DataUbnt]

    def SnmpCompanyName(self, ip):
        shell = subprocess.run(['snmpwalk', '-c', 'public', '-v', '1', ''+ip+'',
                                '1.3.6.1.2.1.2.2.1.6.2'], check=True, capture_output=True)
        udpPort = shell.stdout.decode()
        PureSnmp = udpPort.split(":")[1]
        Puremac = self.MacAdresFind(PureSnmp.replace(" ","")[0:6])
        return Puremac
        
        # -- Api vendors kullanmiyorum 1000 request'dan sonra cevap vermiyor.

    # def MacAdresFindVendor(self, macAdres):
    #     url = "https://api.macvendors.com/"
    #     response = requests.get(url+macAdres)
    #     return(response.content.decode())

    def Lstenpoint(self, ip):
        Company = self.SnmpCompanyName(ip)
        if "Ubiquiti Networks Inc" in Company:
            return self.SnmpUbnt(ip)
        elif "Mimosa Networks" in Company:
            AsyncMimosa = asyncio.run(self.SnmpMimosa(ip))
            Asynm = str(AsyncMimosa[1])[1:3]
            return [Asynm]

        elif "Routerboard.com" in Company:
            return asyncio.run(self.SnmpMikrotik(ip))

    def MacAdresFind(self,Mac):

        connection = mysql.connector.connect(host="192.168.192.2", user="root", password="As081316",
                                            database="PoyrazwifiVerici", auth_plugin='mysql_native_password')
        cursor = connection.cursor()
        cursor.execute(
            'Select Name From MacToName WHERE MAC="'+Mac+'"')
        res = cursor.fetchall()
        for d in res : 
            for scx in d:
                return scx.decode()
[
    # Ubiquiti Networks Inc
    # "Routerboard.com"
    # Mimosa Networks"
]
# Obj = SnmpSignal()

# Dot1 = Obj.SnmpCompanyName('10.101.2.11')
# print(Dot1)
