#!/usr/bin/python3
'''
1.3.6.1.4.1.43356.2.1.2.4.1.0 - Station Wireless Mode - 2
1.3.6.1.4.1.43356.2.1.2.1.1.0 - Cihazin Ismi
1.3.6.1.4.1.43356.2.1.2.4.1.0 -  Hangi Ulke koduna Sahip
1.3.6.1.4.1.43356.2.1.2.5.8.0 - Cihazin Ip Adresi
1.3.6.1.4.1.43356.2.1.2.5.10.0 - Cihazin Gatewayi
1.3.6.1.4.1.43356.2.1.2.6.1 - Cihazin Chain Degerleri
1.3.6.1.4.1.43356.2.1.2.6.1.1.6.1 	- Cihazin Frekansi
1.3.6.1.4.1.43356.2.1.2.6.3.1.3.1 - Cihazin Kac Mhz'de Mhz'si
1.3.6.1.4.1.43356.2.1.2.6.3.1.4.1 - Cihaz Kac dBm'de Calisiyor.
1.3.6.1.4.1.43356.2.1.2.6.3.1.5.1 - Cihaz Kac Frekasnta Calisiyor.
1.3.6.1.4.1.43356.2.1.2.7.1.0 - Cihaz Kac mbps trafik geciyor Tx Degeri
1.3.6.1.4.1.43356.2.1.2.7.2.0 - Cihazin anlik gecirdigi Rx Degeri.

1.3.6.1.4.1.43356.2.1.2.3.3.0	mimosaWanStatus.0	INTEGER: connected(1)	Overview > Dashboard > Wireless Status
1.3.6.1.4.1.43356.2.1.2.3.4.0	mimosaWanUpTime.0	Timeticks: (18571300) 2 days, 3:35:13.00	Overview > Dashboard > Link Uptime
1.3.6.1.4.1.43356.2.1.2.1.8.0	mimosaInternalTemp.0	INTEGER: 382 C1	Overview > Dashboard > Device Details > Internal Temp or CPU Temp (Local)
'''

import os
from routeros_api import Api, CreateSocketError
import aiosnmp
import asyncio
import time
import mysql.connector
import json
import nmap3

def sql():
    connection = mysql.connector.connect(host="127.0.0.1", user="root", password="Password",
                                              database="LinkSnmp", auth_plugin='mysql_native_password')
    cursor = connection.cursor()
    cursor.execute(
        'Select Bname From bras ORDER BY Bname')
    gels = cursor.fetchall()
    nasName = []
    for values in gels:
        nasnameStr = values[0].decode()
        nasName.append(nasnameStr)
    return nasName

async def Snmpdata(ip):
    try:
        degerler = {}
        async with aiosnmp.Snmp(host=ip, port=161, community="public") as snmp:
            getlist = []
            for res in await snmp.get(['1.3.6.1.4.1.43356.2.1.2.1.1.0',
                                    '1.3.6.1.4.1.43356.2.1.2.5.8.0',
                                    '1.3.6.1.4.1.43356.2.1.2.6.3.1.3.1',
                                    '1.3.6.1.4.1.43356.2.1.2.6.1.1.6.1',
                                    '1.3.6.1.4.1.43356.2.1.2.7.1.0',
                                    '1.3.6.1.4.1.43356.2.1.2.6.2.1.5.1',
                                    '1.3.6.1.4.1.43356.2.1.2.6.2.1.5.2',
                                    '1.3.6.1.4.1.43356.2.1.2.7.2.0',
                                    '1.3.6.1.4.1.43356.2.1.2.1.8.0',
                                    '1.3.6.1.4.1.43356.2.1.2.3.3.0',
                                    '1.3.6.1.4.1.43356.2.1.2.6.1.1.3.1',
                                    '1.3.6.1.4.1.43356.2.1.2.6.1.1.3.2',
                                    '1.3.6.1.4.1.43356.2.1.2.6.2.1.2.1',
                                    '1.3.6.1.4.1.43356.2.1.2.6.2.1.2.2',
                                    '1.3.6.1.4.1.43356.2.1.2.6.2.1.5.3',
                                    '1.3.6.1.4.1.43356.2.1.2.6.2.1.5.4',
                                    '1.3.6.1.4.1.43356.2.1.2.6.2.1.2.3',
                                    '1.3.6.1.4.1.43356.2.1.2.6.2.1.2.4',
                                    '1.3.6.1.2.1.2.2.1.5.1']):

                task = asyncio.ensure_future(
                    Apisnmp(res))
                getlist.append(task)
            view = await asyncio.gather(*getlist)
        try:
            mimosaName = view
            NamesMimosa = mimosaName[0].decode()
            MimosaIp = str(mimosaName[1])
            MimosaMhz = mimosaName[2]
            MimosaFrequency = mimosaName[3]
            MimosaTxValue = mimosaName[4] / 100000
            MimosaRxPhy0 = mimosaName[5]
            MimosaRxPhy1 = mimosaName[6]
            MimosaRxValue = mimosaName[7] / 100000
            rxValuess = str(MimosaRxValue)
            rxValues = rxValuess[0:5]
            txValuess = str(MimosaTxValue)
            txValues = txValuess[0:5]
            MimosaCpuTempS = str(mimosaName[8])
            MimosaCpuTemp = MimosaCpuTempS[0:2]
            WirelesStatus = mimosaName[9]
            RxDbms = str(mimosaName[10])
            RxDbms1 = str(mimosaName[11])
            MimosaTxPhy0 = mimosaName[12]
            MimosaTxPhy1 = mimosaName[13]
            MimosaRxPhy2 = mimosaName[14]
            MimosaRxPhy3 = mimosaName[15]
            MimosaTxPhy2 = mimosaName[16]
            MimosaTxPhy3 = mimosaName[17]
            if mimosaName[18] != None:
                Eth0 = int(mimosaName[18]) / 1000000
            else:
                Eth0 = 0
                
            if MimosaRxPhy2 is None:
                MimosaRxPhy2 = 0
                MimosaRxPhy3 = 0
                MimosaTxPhy2 = 0
                MimosaTxPhy3 = 0

            MimosaTotalRxPhy = MimosaRxPhy0 + MimosaRxPhy1 + MimosaRxPhy2 + MimosaRxPhy3
            MimosaTotalTxPhy = MimosaTxPhy0 + MimosaTxPhy1 + MimosaTxPhy2 + MimosaTxPhy3

            RxDbm = RxDbms[0:3]
            RxDbm1 = RxDbms1[0:3]
            Objes = {
                'NamesMimosa': NamesMimosa,
                'MimosaIp': MimosaIp,
                'MimosaMhz': MimosaMhz,
                'MimosaFrequency': MimosaFrequency,
                'MimosaTotalRxPhy': MimosaTotalRxPhy,
                'MimosaTotalTxPhy': MimosaTotalTxPhy,
                'MimosaTxValue': txValues,
                'MimosaRxValue': rxValues,
                'MimosaCpuTemp': MimosaCpuTemp,
                'WirelesStatus': WirelesStatus,
                'RxDbm': RxDbm,
                'RxDbm1': RxDbm1,
                'Ethspeed':Eth0
                }
        except Exception as err:
            print(err)
        degerler.update({"Data": Objes})
        return degerler
    except Exception as err:
        print(err)


async def Apisnmp(res):
    return (res.value)


def DatabaseIp(Qstring, queryStriq):
    connection = mysql.connector.connect(host="127.0.0.1", user="root", password="Password",
                                              database="LinkSnmp", auth_plugin='mysql_native_password')
    cursor = connection.cursor()
    cursor.execute(
        'Select ip From tblLink WHERE device="'+Qstring+'" and nas="'+queryStriq+'"  ORDER BY ip')
    gels = cursor.fetchall()
    list2 = []
    for x in gels:
        for c in x:
            list2.append(str(c.decode()))

    return list2


async def endPoint(Qstring, queryStriq):
    lis2 = []
    
    for d in DatabaseIp(Qstring, queryStriq):
        response = os.system('ping -c 1 -W 1 ' + d + '>> /dev/null 2>&1')
        if response == 0:
            ds = asyncio.ensure_future(Snmpdata(d))
            lis2.append(ds)
        # else:
        #     return [{"Not_Working": "Cihaza ping yok yada snmp kapali Cihaz Aktif Degil."}]

    views = await asyncio.gather(*lis2)
    if views != None:
        return views


