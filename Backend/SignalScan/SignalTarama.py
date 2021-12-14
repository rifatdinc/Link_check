#!/usr/bin/python3
import routeros_api
from .Ftpfiles1 import ftpDownload
import os
from pathlib import Path


def Signal(text):
    getcurend = os.path.realpath(__file__)
    path = Path(getcurend)
    
    liste = []
    with open(os.path.dirname(path.parent.absolute())+'/' + text , encoding='iso-8859-1') as f:
        for x in f:
            ds = x.split(",")
            Accespoints = ds[1]
            Accespointd = Accespoints[1:]
            Accespointc = Accespointd[::-1][1:]
            Accespoint = Accespointc[::-1]
            keyMac = ds[0]
            Signal = ds[3]
            frequency = ds[2][0:4]
            if "poyraz" in Accespoint or "Poyraz" in Accespoint or "RaFi" in Accespoint:

                obsd = {"key": keyMac, "Accespoint": Accespoint,
                        "Signal": Signal, "Frequency": frequency}
                liste.append(obsd)
    print(liste)
    return liste


def ms(e):
    return e["Signal"]


def Resultend(text):

    sd = Signal(text)
    sd.sort(key=ms)
    return sd


def CostumeInfo(ip):
    R1s = routeros_api.Api(ip, "admin", 'password')
    ppoename = R1s.talk('/interface/pppoe-client/print')[0]['user']
    signal = R1s.talk('/interface/wireless/print')[0]
    signals = R1s.talk(
        '/interface/wireless/registration-table/print')
    affet = []
    for sinyal in signals:
        affet.append({
            "ppoename": ppoename,
            "sig1": sinyal['signal-strength-ch0'],
            "sig2": sinyal['signal-strength-ch1'],
            "sig3": sinyal['tx-signal-strength-ch0'],
            "sig4": sinyal['tx-signal-strength-ch1'],
            "radioname": sinyal['radio-name'],

        })
    return affet


def Signalscan(ip):
    R1 = routeros_api.Api(ip, "admin", 'password')
    ppoename = R1.talk('/interface/pppoe-client/print')[0]['user']
    R1.talk('/interface/wireless/scan\n=number=wlan1\n=duration=45\n=save-file='+ppoename+'.txt')
    ftpDownload(ppoename+".txt", ip)
    return Resultend(ppoename+".txt")
