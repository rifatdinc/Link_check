#!/usr/bin/python3
import os
import socket
from RouteroS.routeros_api import Api



api = Api("10.50.1.9", "admin", "mc4152")


print(api.talk('/interface/wireless/print')[0]['mode'])


