#!/usr/bin/python3
import mysql.connector
import json
import os
try:
    from .ubntapi import Ubntos
   
except ImportError:
    from concurrent.futures import ProcessPoolExecutor
    from ubntapi import Ubntos
### -- Mysql Ip List
def qetsql(Nasselect):
    connection = mysql.connector.connect(host="127.0.0.1", user="root", password="Password",
                                         database="PoyrazwifiVerici", auth_plugin='mysql_native_password')
    cursor = connection.cursor()
    cursor.execute(
        'Select distinct ip From tblLink WHERE device="ubnt" and nas="'+Nasselect+'"  and not type="RBLHGG-60ad" ORDER BY ip')
    gels = cursor.fetchall()
    lastList = []
    
    for c in gels:
        
        for xa in c:
            sa = xa.decode()
           
            response = os.system('ping -c 1 -W 0.5 '+ sa + '>> /dev/null 2>&1')
            
            if response == 0:
                
                lastList.append(sa)
    return lastList


## -- Backend Api

def ubnt5gHz(ip):
    sd  = Ubntos()
    a = sd.RSession(ip)
    return a
    
    
def lastubntendpoint(Nasselect):
    lista1 = []
    with ProcessPoolExecutor() as executor:
        r = executor.map(ubnt5gHz,qetsql(Nasselect))
        try:
            
            for x in r:
                if not "60" in  (x['Data']["Data1"]["host"]['devmodel']) or not "GigaBeam Lr" in (x['Data']["Data1"]["host"]['devmodel']):
                    lista1.append(x)
        except Exception as r:
            return json.dumps({"ExceptionErr1":r})
    return lista1
    

    
    


