#!/usr/bin/python3

from flask import Flask
import json
import time
from flask_sqlalchemy import SQLAlchemy
from DatabaseCreate import allmacid,db
# from Mac_AdresInsert import allmacid,db

class searchMac:
        
    def searchEngine(self,mac=''):
        cut =  mac[0:8] # stringi 0 dan baslatip 8 karaktere kadar 
        macSearch = allmacid.query.filter_by(mac=cut).first()
        # return macSearch.macvendor
        if macSearch:
            return macSearch.macvendor
            # print(macSearch.mac)
        else:
            return 'notFmacAdress'
        return macSearch

# fas= searchMac()
# print(fas.searchEngine('C4:AD:34:E4:3D:F6'))