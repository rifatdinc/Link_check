#!/usr/bin/python3
from routeros_api import Api

####### EXAMPLE ###########
import os 
mikpaswd = os.environ.get("mikpaswd")


s = Api(address="192.168.14.35",user="admin",password=mikpaswd)
print(s.create_connection())
print(s.talk('/ip/firewall/nat/print\n?log-prefix=rifatdinc@poyrazwifi'))

nat_find = s.talk('/ip/firewall/nat/print\n?log-prefix=rifatdinc@poyrazwifi')
for x in nat_find:
    print(x)
    s.talk(f'/ip/firewall/nat/remove\n=.id={x[".id"]}')
    
s.close()