from aiohttp import web
from api.history import routes

history = web.Application()

history.router.add_get('', routes.home)
history.router.add_get('/', routes.home)

history.router.add_get('/get_history', routes.get_history)