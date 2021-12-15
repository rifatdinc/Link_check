#!/usr/bin/python3
import mysql.connector
import json
import os
from Db.PoyrazLink import Poyrazdb 
try:
    from .ubntapi import Ubntos
   
except ImportError:
    from concurrent.futures import ProcessPoolExecutor
    from ubntapi import Ubntos
### -- Mysql Ip List

## -- Backend Api
class UbntFivegHz:
    db = Poyrazdb()
        
    def ubnt5gHz(self,ip):
        sd  = Ubntos()
        a = sd.RSession(ip)
        return a
        
    def lastubntendpoint(self,Nasselect):
        lista1 = []
        with ProcessPoolExecutor() as executor:
            
            r = executor.map(self.ubnt5gHz,self.db.ubnt_sql(Nasselect))
            try:
                
                for x in r:
                    if not "60" in  (x['Data']["Data1"]["host"]['devmodel']) or not "GigaBeam Lr" in (x['Data']["Data1"]["host"]['devmodel']):
                        lista1.append(x)
            except Exception as r:
                return json.dumps({"ExceptionErr1":r})
        return lista1
        

        
        


