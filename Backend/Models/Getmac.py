#!/usr/bin/python3

from Db.Linkdb import db, macaddrs


class Classmac:

    def getMac(self, mac):
        Mac_name = db.session.query(macaddrs).filter_by(mac=mac).first()
        if Mac_name is not None:
            db.session.remove()
            return Mac_name.company_name
        else:
            return False
