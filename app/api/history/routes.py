import json

from aiohttp.web import Response

from aiohttp_jinja2 import template

from extensions import labmaColl
from constants import mapUrls
from utils import localizeNaiveTimeStampInBR

places = mapUrls.keys()

@template('history.html')
async def home(request):
    return None

async def get_history(request):
    limit = 10
    if 'limit' in request.rel_url.query:
        limit = int(request.rel_url.query['limit'])
    
    res = list()
    for row in labmaColl.find().sort('timestamp', -1).limit(limit):
        aux = { 'timestamp': localizeNaiveTimeStampInBR(row['timestamp'])}
        for place in places:
            aux[place] = row[place]['status']
        res.append(aux)   

    response_obj = { 'header' : mapUrls, 'data': res }

    return Response(text=json.dumps(response_obj))
