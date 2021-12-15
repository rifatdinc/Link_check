
import mysql.connector
import os
class Poyrazdb():
    def __init__(self) -> None:
        self.linkpwd = os.environ.get("linpaswd")
        self.dbuser = os.environ.get("dbuser")
        self.dbpasswd = os.environ.get("dbpasswd")
        self.dbhost = os.environ.get("host")
        self.dbdatabase = os.environ.get("dbdatabase")
        print(self.dbdatabase)
        self.connection = mysql.connector.connect(host=self.dbhost, user=self.dbuser, password=self.dbpasswd,
                                                database=self.dbdatabase, auth_plugin='mysql_native_password')
    
    def ubnt_sql(self,Nasselect):
        cursor = self.connection.cursor()
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
    
    def MimosaIp(self,Qstring, queryStriq):
        cursor = self.connection.cursor()
        cursor.execute('Select ip From tblLink WHERE device="'+Qstring+'" and nas="'+queryStriq+'"  ORDER BY ip')
        gels = cursor.fetchall()
        list2 = []
        for x in gels:
            for c in x:
                list2.append(str(c.decode()))

        return list2

    def nas_listIP(self):
        cursor = self.connection.cursor()
        cursor.execute('Select Bip From bras ORDER BY Bip DESC')
        result = cursor.fetchall()
        Word = []
        for x_ in result:
            for s in x_:
                Word.append(s.decode())

        return Word
    
    
    def Mikrotik5gHz_db(self, Qstring, queryStriq):
        cursor = self.connection.cursor()
        cursor.execute(
            'Select distinct device,nas,ip From tblLink WHERE device="'+Qstring+'" and nas="'+queryStriq+'"  and not type="RBLHGG-60ad" ORDER BY ip')
        gels = cursor.fetchall()
        lsa = []
        for xd in gels:
            qet = xd[2].decode()
            if qet not in lsa:
                dd = qet.replace(" ", "")
                lsa.append(dd)

        return lsa
    
    
    def Mikrotik60gHz_db(self,):
        cursor = self.connection.cursor()
        cursor.execute('Select distinct ip From tblLink WHERE type="RBLHGG-60ad" ORDER BY ip'
        )
        res = cursor.fetchall()
        sd = []
        for xs in res:
            for xd in xs:
                sd.append(xd.decode())
        return sd
    
    
    def MacAdresFind(self,Mac):

        cursor = self.connection.cursor()
        cursor.execute('Select Name From MacToName WHERE MAC="'+Mac+'"')
        res = cursor.fetchall()
        for d in res : 
            for scx in d:
                return scx.decode()
