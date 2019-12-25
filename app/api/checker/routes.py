from json import dumps as json_dumps

from aiohttp.web import Response
from aiohttp_jinja2 import template

@template('checker.html')
async def home(request):
    return None

async def check(request):
    return Response(text=json_dumps({'status': 'fail'}))