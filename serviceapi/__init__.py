import logging

from flask import Flask
from flask.ext.cors import CORS
from flask.ext.sqlalchemy import SQLAlchemy

from serviceapi import settings
from serviceapi.core import setup_routing


# TODO: Add ratelimiting API

# setup application
app = Flask('serviceapi')
app.config.from_object(settings)

# setup database
db = SQLAlchemy(app)
# setup cors
cors = CORS(
    app,
    resources={
        r"/v1/*": {
            "origins": settings.CORS_ORIGINS
        }
    }
)

# register application views and blueprints
from serviceapi.urls import routes
setup_routing(app, routes)
