from aiohttp import web

from extensions import CFG
from api.app import create_app


web_app = create_app()