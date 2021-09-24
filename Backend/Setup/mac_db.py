#!/usr/bin/python3
import csv
from Db import Linkdb
db = Linkdb.db

class Macdb:
    def Dbadd(self):
        with open('./Setup/mac_vendor.csv', mode='r') as csv_file:
            csv_ = csv.reader(csv_file, delimiter=',')
            for row in csv_:
                mac_Adress = row[0]
                vendor_name = row[2]
                addmac = Linkdb.mac_vendor(mac=mac_Adress, company_name=vendor_name)
                db.session.add(addmac)
                db.session.commit()
