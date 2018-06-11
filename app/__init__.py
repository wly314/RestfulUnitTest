#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api

from app.config import config

app_api = Api()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    app_api.app = app
    app_api.init_app(app)
    configure_resources(app_api)

    return app


# register API blueprint 注册资源路由
def configure_resources(a_api):
    from app.api import RESOURCES
    for resource, prefix in RESOURCES:
        a_api.add_resource(resource, prefix)
