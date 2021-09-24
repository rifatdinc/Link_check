#!/usr/bin/python3

from Db.Linkdb import db,mac_vendor

class Classmac:
    
    def getMac(self,where):
        db.session.query(mac_vendor).filter_by(mac='')