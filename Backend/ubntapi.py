#!/usr/bin/python3.8
import ssl
from typing import AsyncContextManager
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import urllib3
import requests
import asyncio
import aiohttp
from requests.api import head
try:

    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    from requests.sessions import Session, session
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
except ConnectionError as r:
    print(r)


class Ubntos():

    def ubntAuth(self, ip):
        return 'https://'+ip+'/api/auth'

    def urlsapi(self, ip):
        return [
            'http://'+ip+'/arp.cgi',
            'http://'+ip+'/sroutes.cgi',
            'http://'+ip+'/status.cgi',
        ]

    def RSession(self, ip):

        self.responses_by_ip = {}
        with requests.Session()as s:
            r = s.post(
                url=self.ubntAuth(ip),
                data={
                    'username': 'ubnt',
<<<<<<< HEAD
                    'password': 'Mc4152..'
                }, verify=False,
=======
                    'password': 'Password'
                },verify=False,
>>>>>>> fab32dc4c47bbd3a6ea2f71e6a0f106602f28d0f
                timeout=5)
            self.responses = {}
            for url in self.urlsapi(ip):
                r = s.get(url=url, verify=False)

                self.responses.update(
                    {"Ip": ip, "Data1": r.json() if r.status_code == 200 else r.status_code})
            # print(self.responses['Ip'])
            self.responses_by_ip.update({"Data": self.responses})
        return self.responses_by_ip

    def ubnt60ghzList(self):
        return [
            '10.131.1.2',
            '10.131.1.3',
            '10.126.1.3',
            '10.126.1.4',
            # '10.104.1.131',
            # '10.104.1.130',
            '10.117.13.2',
            '10.117.13.3',
            '10.129.7.50',
            '10.129.7.51',
            '10.130.4.6',
            '10.130.4.5',
            '10.107.0.5',
            '10.107.0.6',
            '10.120.4.54',
            '10.120.4.55'
        ]

    def endPoint(self):
        kls = []
        with ProcessPoolExecutor() as executor:
            result = executor.map(self.RSession, self.ubnt60ghzList())
            for x in result:
                kls.append(x)

        return kls


if __name__ == '__main__':
    Ubntos()
