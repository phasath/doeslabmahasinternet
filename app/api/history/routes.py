import json

from aiohttp import web

async def home(request):
    response_obj = { 'status' : 'success', 'location': 'history' }
    return web.Response(text=json.dumps(response_obj))
