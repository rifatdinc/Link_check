#!/usr/bin/python3
import mysql.connector

def RouterIp():
    connection = mysql.connector.connect(host="192.168.192.2", user="root", password="As081316",database="PoyrazwifiVerici", auth_plugin='mysql_native_password')
    cursor = connection.cursor()
    cursor.execute('Select Bip From bras ORDER BY Bip DESC')
    result = cursor.fetchall()
    return result