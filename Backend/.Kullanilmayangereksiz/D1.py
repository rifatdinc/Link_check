#!/usr/bin/python3
import aiohttp
import asyncio
import requests
from requests.sessions import session
async def x(i):
    print(f"start {i}")
    await asyncio.sleep(1)
    print(f"end {i}")
    return i

# run x(0)..x(10) concurrently and process results as they arrive
async def A():
  
  for f in asyncio.as_completed([x(i) for i in range(10)]):
    result = await f
    
asyncio.run(A())