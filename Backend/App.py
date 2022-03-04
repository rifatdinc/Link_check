#!/usr/bin/python3
import os
from flask import Flask, request
from flask_cors import CORS
from Db.PoyrazLink import Poyrazdb
from snmp import Mimosa
from Mikrotik import Mikrotik
from Mik60ghz import Mik60gHz
from ubntapi import Ubntos
from SignalScan import SignalTarama
from SignalScan.Connectscan import qscancon
from Ubnt5 import UbntFivegHz
from SignalResponse.SignalSend import SnmpSignal
import asyncio
import json
from Models.MsystemPrivate import Apimsystem, Mikrotik_Nas
import hashlib
from datetime import timedelta
from flask_jwt_extended import (
    create_access_token,
    get_jwt,
    jwt_required,
    current_user,
    JWTManager,
    get_jwt_identity,
)

app = Flask(__name__)
CORS(app)
jwt = JWTManager(app)
Obj = SnmpSignal()
app.config["JWR_SECRET_KEY"] = "219837129837127398123"
app.secret_key = "somesecretkeythatonlyis"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=49)


@app.route("/Login", methods=["POST"])
def Loginpage():
    data = json.loads(request.data)
    username = data["username"]
    password = data["password"]
    dbcheck = Poyrazdb().LoginPage(username)
    passwd = hashlib.sha1(password.encode()).hexdigest()
    if dbcheck:
        if username == dbcheck["Username"] and dbcheck["Password"] == passwd:
            print("Login Success")
            addi = {"Role": dbcheck["Role"]}
            access_token = create_access_token(identity=username, additional_claims=addi)
            return json.dumps({"access_token": access_token}), 200
        else:
            return json.dumps({"error": "Invalid credentials"}), 401
    else:
        return json.dumps({"error": "Invalid credentials"}), 401


@app.route("/nasdata")
@jwt_required()
def gets():
    return json.dumps(Poyrazdb().bras())


@app.route("/nasdatavalue")
@jwt_required()
def get_value():
    return json.dumps(Poyrazdb().brasses())


@app.route("/Speaksignal", methods=["POST"])
@jwt_required()
def SpeaksSignals():
    return Obj.Lstenpoint(json.loads(request.data))


@app.route("/getdatasql", methods=["POST"])
@jwt_required()
def sardata():
    data = json.loads(request.data)
    Dats = asyncio.run(Mimosa().endPoint("mimosa", data["Clickdata"].replace(" ", "")))
    return json.dumps(Dats)


@app.route("/mikrotik", methods=["POST"])
@jwt_required()
def Mikrotikdata():
    m = Mikrotik()
    data = json.loads(request.data)
    return json.dumps(m.LastFunc("mikrotik", data["Clicks"].replace(" ", "")))


@app.route("/Mik60ghz")
@jwt_required()
def Mik60GHZ():
    return Mik60gHz().Lastendpoint()


@app.route("/ubnt60ghz")
@jwt_required()
def ubnt60():
    return Ubntos().endPoint()


@app.route("/ubnt5gHz", methods=["POST"])
@jwt_required()
def ubnt5ghz_():
    return UbntFivegHz().lastubntendpoint(json.loads(request.data))


@app.route("/signalscan", methods=["POST"])
@jwt_required()
def signalscan():
    return SignalTarama.Signalscan(json.loads(request.data)["Data"])


@app.route("/scanconnect", methods=["POST"])
@jwt_required()
def scanconnect():
    data = json.loads(request.data)
    S = qscancon(
        data["Ipadress"], data["Accespoint"], data["Frequency"], data["pppoename"]
    )
    return json.dumps(S)


@app.route("/realdatascan", methods=["POST"])
@jwt_required()
def realdatascan():
    return SignalTarama.CostumeInfo(json.loads(request.data))


@app.route("/find_fail", methods=["POST"])
@jwt_required()
def find_fail():
    data = Mikrotik_Nas().Nas_List(json.loads(request.data))
    return {}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
