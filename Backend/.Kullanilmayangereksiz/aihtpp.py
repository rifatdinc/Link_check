#!/usr/bin/python3.8
import ssl
from typing import AsyncContextManager
from concurrent.futures import ProcessPoolExecutor
import urllib3
import requests
import asyncio
import aiohttp
from requests.api import head
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests.sessions import Session, session
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


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

        self.responses_by_ip = []
        with requests.Session()as s:
            r = s.post(
                url=self.ubntAuth(ip),
                data={
                    'username': 'ubnt',
                    'password': 'Mc4152..'
                },
                verify=False,
                timeout=5
            )
            print(r.status_code)


            # if r.status_code > 201:
            #     pass
            self.responses = {}
            for url in self.urlsapi(ip):
                url = url.format(ip)
                # print(url)

                r = s.get(
                    url=url,
                    verify=False
                )

                self.responses.update(
                    {"Ip": ip, "Data1": r.json() if r.status_code == 200 else r.status_code})
            self.responses_by_ip.append({"Data": self.responses})
        return self.responses_by_ip

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
        kls = []
        with ProcessPoolExecutor() as executor:
            result = executor.map(self.RSession, self.ubnt60ghzList())
            for x in result:
                for l in x:
                    kls.append(l)
        return kls
        # lis2 = []
        # for d in self.ubnt60ghzList():
        #     lis2.append(self.RSession(d))
        # return lis2


m = Ubntos()
print(m.endPoint())
# for x in cs:
#     for l in x:
#         print(l)

# When I post my session information, I get 200 arrows. But when I make a request to a different url, I get 403. I would be very grateful if you could help.

# I'm doing the synchronous version of this with the request library. I'm getting the results. Thank you for everything.

# ```
#     def urlsapi( ip):
#         return ['http://'+ip+'/arp.cgi',
#             'http://'+ip+'/sroutes.cgi',
#             'http://'+ip+'/status.cgi']

# async def RSession( ip):

#         responses_by_ip = {}

#         async with aiohttp.ClientSession()as session:
#             async with session.post(
#                 url='https://'+ip+'/api/auth',
#                 data={'username': 'username','password': 'password'},
#                 ssl=False,timeout=5)as Err:
#                 responses = []
#                 for url in urlsapi(ip):
#                     url = url.format(ip)

#                     task = asyncio.ensure_future(
#                         qetqetir(url, session, ip))
#                     responses.append(task)
#                 view = await asyncio.gather(*responses)
#                 responses_by_ip.update({"Data": view})


#         return responses_by_ip

# async def qetqetir( url, session, ip):
#     r = await session.get(url=url,ssl=False)
#     return({"Ip": ip, "Data1": r.json() if r.status == 200 else r.status})

#  async def endPoint(:
#         lis2 = []

#         for d in  ubnt60ghzList():
#            ds = asyncio.ensure_future(RSession(d))
#            lis2.append(ds)
#         views = await asyncio.gather(*lis2)
#         print(views)

#         return lis2


# d = Ubntos()
# asyncio.run(d.endPoint())


# ```


# Output:

# ```
# POST
# 200
# POST

# 403
# GET
# 403
# ```
