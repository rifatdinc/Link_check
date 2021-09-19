#!/usr/bin/python3
import ssl
import requests
from concurrent.futures import ThreadPoolExecutor
import asyncio
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import aiohttp
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


login_url = 'https://10.131.1.3/api/auth'


def ubntAuth(ip):
    return 'https://'+ip+'/api/auth'


def urlsapi(ip):
    return [
        'http://'+ip+'/arp.cgi',
        'http://'+ip+'/sroutes.cgi',
        'http://'+ip+'/status.cgi',
    ]


async def authpost(session: aiohttp.ClientSession,ip) -> None:
    print("Query http://httpbin.org/basic-auth/andrew/password")
    async with session.post('https://'+ip+'/api/auth',ssl=False,data={'username': 'ubnt','password': 'Mc4152..'}) as resp:
        print(resp.status)
        # # body = await resp.()
        # # print(body)
        # async with 

async def go(ip) -> None:
    async with aiohttp.ClientSession(
        # auth=aiohttp.BasicAuth("ubnt", "Mc4152..")
    ) as session:
        await authpost(session,ip)
        sd = await session.get( 'http://'+ip+'/status.cgi',ssl=False)
        
        print(sd)


loop = asyncio.get_event_loop()
loop.run_until_complete(go('10.131.1.2'))


async def RSession(ip):

    responses_by_ip = {}

    async with aiohttp.ClientSession()as session:
        # aiohttp.BasicAuth
        async with session.post(
            url=ubntAuth(ip),
            data={
                'username': 'ubnt',
                'password': 'Mc4152..'
            },
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'},
                ssl=False, timeout=5)as Err:
            # assert Err.status == 200
            print(await Err.text())

            responses = []
            for url in urlsapi(ip):
                url = url.format(ip)

                task = asyncio.ensure_future(
                    qetqetir(url, session, ip))
                responses.append(task)
            view = await asyncio.gather(*responses)
            responses_by_ip.update({"Data": view})

    return responses_by_ip


async def qetqetir(url, session, ip):

    r = await session.get(url=url, ssl=False)
    print(r.status)
    return({"Ip": ip, "Data1": r.json() if r.status == 200 else r.status})


def ubnt60ghzList():
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


async def endPoint():
    lis2 = []

    for d in ubnt60ghzList():
        ds = asyncio.ensure_future(RSession(d))
        lis2.append(ds)
    views = await asyncio.gather(*lis2)
    print(views)

    return lis2


# # d = Ubntos()
# asyncio.run(endPoint())
