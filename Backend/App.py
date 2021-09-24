#!/usr/bin/python3
from flask import Flask, request
from flask_cors import CORS
from snmp import sql, endPoint, DatabaseIp
from Mikrotik import Mikrotik
from Mik60ghz import Lastendpoint
from ubntapi import Ubntos
from SignalScan import SignalTarama
from SignalScan.Connectscan import qscancon
from Ubnt5 import lastubntendpoint
from Signalsend.SignalSends import SnmpSignal
import aiosnmp
import asyncio
import json
app = Flask(__name__)
CORS(app)
Obj = SnmpSignal()

@app.route('/nasdata')
def gets():
    return json.dumps(sql())

@app.route('/Speaksignal',methods=['POST'])
def SpeaksSignals():
    data = json.loads(request.data.decode())

    Dot1 = Obj.Lstenpoint(data["IpaddressSpeak"])
    return json.dumps(Dot1)

@app.route('/getdatasql', methods=["POST"])
def sardata():

    data = json.loads(request.data.decode())

    Pors = DatabaseIp('mimosa', data['Clickdata'])
    
    Dats = asyncio.run(endPoint('mimosa', data['Clickdata'].replace(" ","")))
    print(Dats)
    return json.dumps(Dats)


@app.route('/mikrotik', methods=['POST'])
def Mikrotikdata():
    m = Mikrotik()
    data = json.loads(request.data.decode())
    Data = m.LastFunc('mikrotik', data['Clicks'].replace(" ",""))
    return json.dumps(Data)


@app.route('/Mik60ghz')
def Mik60GHZ():
    Data = Lastendpoint()

    return json.dumps({"Data": Data})


@app.route('/ubnt60ghz')
def ubnt60():
    d = Ubntos()
    return json.dumps(d.endPoint())

@app.route('/ubnt5gHz', methods=['POST'])
def ubnt5ghz_():
    data = json.loads(request.data.decode())
    Data = lastubntendpoint(data['Clicks'].replace(" ",""))
    return json.dumps(Data)


@app.route('/signalscan',methods=['POST'])
def signalscan():
    data = json.loads(request.data.decode())
    signaldata = SignalTarama.Signalscan(data['Data'])
    return json.dumps(signaldata)




@app.route('/scanconnect',methods=['POST'])
def scanconnect():
    data = json.loads(request.data.decode())
    S = qscancon(data['Ipadress'],data['Accespoint'],data['Frequency'],data['pppoename'])
    return json.dumps(S)


@app.route('/realdatascan',methods=['POST'])
def realdatascan():
    data = json.loads(request.data.decode())
    Costumerinfo = SignalTarama.CostumeInfo(data["Ipadress"])
    return json.dumps(Costumerinfo)




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000,)
