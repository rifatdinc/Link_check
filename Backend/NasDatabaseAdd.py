#!/usr/bin/python3
# from routeros_api import Api
import mysql.connector
# from DatabaseCreate import nas,link,db

def NasAdPostgres():
    connection = mysql.connector.connect(host="127.0.0.1", user="root", password="Passwod",
                                             database="Link_Snmp", auth_plugin='mysql_native_password')
    cursor = connection.cursor()
    cursor.execute('Select Bname,Bip From bras')
    result = cursor.fetchall()
    for ix in result:
        xs = ix
        nasIp = xs[0]
        naname = xs[1]
        NasIp = nasIp.decode()
        NasName = naname.decode()
    
        dbPostgre = nas(NasIp,NasName)
        db.session.add(dbPostgre)
        db.session.commit()

def Mimosalink():
    connection = mysql.connector.connect(host="127.0.0.1", user="root", password="Passwod",
                                             database="Link_Snmp", auth_plugin='mysql_native_password')
    cursor = connection.cursor()
    cursor.execute('Select device,nas,ip From tblLink')
    result = cursor.fetchall()
    lists = []
    for c in result:
        # print(c)
        device = c[0].decode()
        nas = c[1].decode()
        NasIpp = c[2].decode()
        # print(device,nas,NasIpp)
        lists.extend([device,nas,NasIpp])

    return lists
