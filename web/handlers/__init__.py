from web.handlers.api import api


def init_app(app):
    api.init_app(app)