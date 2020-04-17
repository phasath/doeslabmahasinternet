import pytz

from asyncio import (gather, create_task)
from json import dumps as json_dumps
from datetime import datetime

from aiohttp import (ClientSession, TCPConnector)
from aiohttp.web import Response
from aiohttp_jinja2 import template

from extensions import labmaColl
from constants import mapUrls
from utils import localizeTimeStampInBR

@template('checker.html')
async def home(request):
    return None

async def fetch(session, place) -> tuple:    
    url = mapUrls[place]
    async with session.get(url, timeout=.1) as response:
        if response.status != 200:
            response.raise_for_status()
        return (place, response.status)

async def fetch_all(session, places) -> list:
    results = await gather(*[create_task(fetch(session, place))
                                   for place in places])
    return results

async def generate_requests() -> list:    
    urls = mapUrls.keys()
    async with ClientSession(connector=TCPConnector(verify_ssl=False)) as session:
        responses = await fetch_all(session, urls)
        return responses

async def insertDbData(data) -> None:
    res = dict()
    res['timestamp'] = datetime.utcnow()

    for place, status in data.items():
        res[place] = {'uri': mapUrls[place], 'status': status}
    
    if (data['LABMA'] >= 400):
        res['status'] = 'fail'
    else:
        res['status'] = 'success'

    labmaColl.insert_one(res)

async def check(request) -> Response:
    data = await generate_requests()
    data = dict(data)
    
    process = insertDbData(data)
    
    res = dict()
    
    res['responses'] = data

    if (data['LABMA'] >= 400):
        res['status'] = 'fail'
    else:
        res['status'] = 'success'


    res['timestamp'] = localizeTimeStampInBR(datetime.utcnow())
    
    await process
    
    return Response(text=json_dumps(res))
