import json

from aiohttp import web
from aiohttp_jinja2 import setup as jinja2_setup
from jinja2 import FileSystemLoader
from api import (checker, history)
from api.checker.routes import home as default_entry_point
from extensions import CFG


def create_app() -> web.Application:
    """An application factory
    """
    app = web.Application()
    
    register_extensions(app)
    register_nested_apps(app)

    return app

def register_extensions(app: web.Application) -> None:
    """ Register extensions on app
    """

    jinja2_setup(app,
        loader=FileSystemLoader(CFG.TEMPLATE_FOLDER))
    app['static_root_url'] = '/static'
    app.router.add_static('/static/', path=CFG.STATIC_FOLDER, name='static')
    
    return None

def register_nested_apps(app: web.Application) -> None:

    """ Joining nested apps for using like Flask's blueprints
    :param app: The app web.Application from aiohttp
    """
    app.router.add_get('/', default_entry_point)
    app.add_subapp('/check', checker)
    app.add_subapp('/history', history)

    return None
    