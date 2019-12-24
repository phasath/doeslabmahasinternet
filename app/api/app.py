import json

from aiohttp import web
from api import (checker, history)

def create_app():
    """An application factory
    """
    app = web.Application()

    register_nested_apps(app)

    return app

def register_nested_apps(app: web.Application) -> web.Application:

    """ Joining nested apps for using like Flask's blueprints
    :param app: The app web.Application from aiohttp
    """

    app.add_subapp('/check', checker)
    app.add_subapp('/history', history)
    return app

