#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask_restful import Resource


class HomeRes(Resource):
    def get(self):
        name = request.args.get('name')
        return {'hello': '{}'.format(name)}

    def delete(self):
        user_id = request.form.get('user_id')
        try:
            user_id = int(user_id)
        except Exception, e:
            return e.message
        return {'buy-buy': '{}'.format(user_id)}

