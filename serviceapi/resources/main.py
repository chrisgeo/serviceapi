from flask import Blueprint
import json

main = Blueprint('main', __name__)


def index(name=None):
    return json.dumps({'status': 'up'})
