from aiohttp import web
from api.checker import routes

checker = web.Application()

# checker.router.add_get('', routes.home, name='checker')
# checker.router.add_get('/', routes.home)
checker.router.add_get('/run', routes.check)