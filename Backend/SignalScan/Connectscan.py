#!/usr/bin/python3

from .routeros_api import Api
import os
from pathlib import Path


def qscancon(ipadres,accespoint,frequency,ppoeadress):
    r = Api(ipadres,'admin','mc4152')
    getcurend = os.path.realpath(__file__)
    path = Path(getcurend)
    ################## TRY BLOKLARINI SIL
    try:
        print(getcurend)
        print(r)
        r.talk('/file/remove\n=numbers='+ppoeadress+'.txt')
    except Exception:
        pass
    r.talk('/interface/wireless/set\n=numbers=wlan1\n=scan-list=5000-6000\n=frequency-mode=superchannel\n=country=no_country_set\n=ssid='+accespoint+'\n=antenna-gain=0')
    Sonuc = r.talk('/tool/bandwidth-test\n=address=10.1.1.1\n=user=hiztesti\n=password=hiztesti\n=duration=10s\n=protocol=tcp')
    os.path.dirname(path.parent.absolute())
    os.remove(ppoeadress+'.txt')
    print(sonuc)
    return Sonuc
