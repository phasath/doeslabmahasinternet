import json

from aiohttp import web

from aiohttp_jinja2 import template

@template('history.html')
async def home(request):
    return None

async def get_history(request):
    response_obj = { 'status' : 'success', 'location': 'get_history' }
    return web.Response(text=json.dumps(response_obj))
