#!/usr/bin/python3
import ipaddress
import json
import mysql.connector
import os



class Poyrazdb:
    def __init__(self):
        self.linkpwd = os.environ.get("linpaswd")
        self.dbuser = os.environ.get("dbuser")
        self.dbpasswd = os.environ.get("dbpasswd")
        self.dbhost = os.environ.get("host")
        self.dbdatabase = os.environ.get("dbdatabase")
        self.connection = mysql.connector.connect(
            host=self.dbhost,
            user=self.dbuser,
            password=self.dbpasswd,
            database=self.dbdatabase,
            auth_plugin="mysql_native_password",
        )

    def ubnt_sql(self, Nasselect):

        cursor = self.connection.cursor()
        cursor.execute(
            'Select distinct ip From tblLink WHERE device="ubnt" and nas="'
            + Nasselect
            + '"  and not type="RBLHGG-60ad" ORDER BY ip'
        )
        gels = cursor.fetchall()
        lastList = []

        for c in gels:
            for xa in c:
                lastList.append(xa.decode())
        print(lastList)
        return lastList

    def MimosaIp(self, Qstring, queryStriq):
        cursor = self.connection.cursor()
        cursor.execute(
            'Select ip From tblLink WHERE device="'
            + Qstring
            + '" and nas="'
            + queryStriq
            + '"  ORDER BY ip'
        )
        gels = cursor.fetchall()
        list2 = []
        for x in gels:
            for c in x:
                list2.append(str(c.decode()))

        return list2

    def nas_listIP(self):
        cursor = self.connection.cursor()
        cursor.execute("Select Bip From bras ORDER BY Bip DESC")
        result = cursor.fetchall()
        Word = []
        for x_ in result:
            for s in x_:
                Word.append(s.decode())
        print(Word)
        return Word

    def Mikrotik5gHz_db(self, Qstring, queryStriq):
        cursor = self.connection.cursor()
        cursor.execute(
            'Select distinct device,nas,ip From tblLink WHERE device="'
            + Qstring
            + '" and nas="'
            + queryStriq
            + '"  and not type="RBLHGG-60ad" ORDER BY ip'
        )
        gels = cursor.fetchall()
        lsa = []
        for xd in gels:
            qet = xd[2].decode()
            if qet not in lsa:
                dd = qet.replace(" ", "")
                lsa.append(dd)

        return lsa

    def Mikrotik60gHz_db(
        self,
    ):
        cursor = self.connection.cursor()
        cursor.execute(
            'Select distinct ip From tblLink WHERE type="RBLHGG-60ad" ORDER BY ip'
        )
        res = cursor.fetchall()
        sd = []
        for xs in res:
            for xd in xs:
                sd.append(xd.decode())
        return sd

    def MacAdresFind(self, Mac):

        cursor = self.connection.cursor()
        cursor.execute('Select Name From MacToName WHERE MAC="' + Mac + '"')
        res = cursor.fetchall()
        for d in res:
            for scx in d:
                return scx.decode()

    def bras(self):
        cursor = self.connection.cursor()
        cursor.execute("Select Bname,Bip From bras ORDER BY Bname")
        gels = cursor.fetchall()
        nasName = []
        for values in gels:
            nasName.append(values[0].decode())
        
        return nasName
    
    def brasses(self):
        cursor = self.connection.cursor()
        cursor.execute("Select Bname,Bip From bras ORDER BY Bname")
        gels = cursor.fetchall()
        nasName = []
        sayac = 0
        for values in gels:
            sayac +=1
            nasnameStr = values[0].decode()
            nasIp = values[1].decode()
            nasName.append({"key":sayac,"value":nasnameStr,"title":nasIp})
        
        return nasName

    def IssmanagerRadius(self, data):
        connector = mysql.connector.connect(
            host="31.145.42.4",
            user="uzak",
            password="123456+aA",
            db="radius",
            auth_plugin="mysql_native_password",
        )
        cursor = connector.cursor()
        cursor.execute(
            f"Select username From radacct where callingstationid='{data}' order by radacctid desc limit 1 "
        )
        res = cursor.fetchall()
        return res[0][0]

    def LoginPage(self,data):
        connector = mysql.connector.connect(
            host="31.145.42.3",
            user="uzak",
            password="123456+aA",
            db="poyrazwi_wifi41",
            auth_plugin="mysql_native_password",
        )
        cursor = connector.cursor()
        cursor.execute(f"Select username,password,yetki From personel where username='{data}'")
        result = cursor.fetchall()
        print('aslkdsand',result)
        if result != []:
            for x in result:
                return {"Username":x[0],"Password":x[1],"Role":x[2]}
            
        else:
            return False