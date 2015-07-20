import json
import logging

from flask import Blueprint, make_response
from flask_restful import Api, Resource


"""
    To allow mutliple endpoint respresentations
    for getting data, we subclass the Api object
    and write out own parser for output.
"""


def output_csv(data, code, headers=None):
    pass


def output_json(data, code, headers=None):
    """Makes a Flask response with a JSON encoded body"""
    resp = make_response(json.dumps(data), code)
    resp.headers.extend(headers or {})
    return resp


class Api(Api):
    def __init__(self, *args, **kwargs):
        super(Api, self).__init__(*args, **kwargs)
        self.representations = {
            # 'text/csv': output_csv,
            'application/json': output_json,
        }


class CustomConfig(Resource):
    def get(self, id):
        return {'hello': 'world'}

    def post(self):
        pass

    def patch(self, id):
        pass

    def delete(self, id):
        pass

# add api to blueprint
api_vone = Blueprint('api_v1', __name__)
api = Api(api_vone, prefix='/v1')
api.add_resource(CustomConfig, '/config/<int:id>')
