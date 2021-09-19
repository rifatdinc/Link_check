#!/usr/bin/python3

from mac_addressSelect import searchMac
from DatabaseCreate import link, nas, db


def Getselectbras(nas, device):
    # asa = link.query.filter_by('gozlemen2').first()
    # print(asa)
    # rs = db.engine.execute(
    #     "Select * from link WHERE nas = '"+nas+"' and device = '"+device+"'")
    rs = link.query.filter_by(nas=nas,device=device).all()
    information = []
    for row in rs:
        information.append(row)
    return information
# ass = getSelect('Gozlemen2','mimosa')

def Getbras(nas, ip, device):
    sef = {
        'device': device,
        'Ip': ip,
        'nas': nas
    }
dene = verboseS()


dene.getLinkBrand('Ip Adresiniz')
print(getSelect('Gozlemen2', 'mimosa')

