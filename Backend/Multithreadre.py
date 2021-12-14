#!/usr/bin/python3
import concurrent
import requests
import asyncio
from concurrent.futures import ThreadPoolExecutor
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests.sessions import Session, session
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


login_url = 'https://10.131.1.3/api/auth'


class Ubntos():

    def ubntAuth(self, ip):
        return 'https://'+ip+'/api/auth'

    def urlsapi(self, ip):
        return [
            'http://'+ip+'/arp.cgi',
            'http://'+ip+'/sroutes.cgi',
            'http://'+ip+'/status.cgi',
        ]
    

    async def RSession(self, ip):
        self.responses_by_ip = {}
        with ThreadPoolExecutor(max_workers=100) as executor:
            with requests.Session()as session:
                session.post(
                    url=self.ubntAuth(ip),
                    data={
                        'username': 'ubnt',
                        'password': 'Mc4152..'
                    },
                    verify=False,
                    timeout=5
                )

                # if r.status_code > 201:
                #     pass
                self.responses = {}
                for url in self.urlsapi(ip):
                    url = url.format(ip)

                    task = asyncio.ensure_future(
                        self.qetqetir(url, session, ip))
                    self.responses.append(task)
                view = await asyncio.gather(*self.responses)

            self.responses_by_ip.update({"Data": self.responses})
            return self.responses_by_ip

    def qetqetir(self,url,session,ip):
        url = url.format(ip)
        
        with session.get(url=url,verify=False) as r:
            print( {"Ip": ip, "Data1": r.json() if r.status_code == 200 else r.status_code})

    def ubnt60ghzList(self):
        return [
            '10.131.1.2',
            '10.131.1.3',
            '10.126.1.3',
            '10.126.1.4',
            '10.126.1.4',
            '10.104.1.131',
            '10.104.1.130',
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
        lis2 = []
        for d in self.ubnt60ghzList():
            lis2.append(self.RSession(d))
        return lis2


d = Ubntos()
d.endPoint()
# print(d.RSession('10.131.1.2'))
