from aiohttp import web

from extensions import CFG
from api.app import create_app


web_app = create_app()

if CFG.ENV == 'development':
    web.run_app(web_app, host=CFG.AIO_HOST, port=CFG.AIO_PORT)