#!/usr/bin/python3

from pyzabbix import ZabbixAPI
import time
from datetime import datetime

zapi = ZabbixAPI('http://192.168.192.102/zabbix')

zapi.login('Admin','zabbix')


item_id = '125082'

# Create a time range

history = zapi.history.get(itemids=[item_id],
                           output='extend',
                           limit='5000',
                           )
if not len(history):
    history = zapi.history.get(itemids=[item_id],
                               output='extend',
                               limit='5000',
                               history=0,
                               )

for point in history:
    print(point)
    print("{0}: {1}".format(datetime.fromtimestamp(int(point['clock']))
                            .strftime("%x %X"), point['value']))