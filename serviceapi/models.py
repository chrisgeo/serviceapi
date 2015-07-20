from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import (
    func
)
from sqlalchemy.dialects.postgresql import JSON

from serviceapi import db


class AutoInitMixin(object):
    """
    Mixin for populating models columns automatically (no need
    to define an __init__ method) and set the default value if any.
    Also sets the model id and __tablename__ automatically.
    """
    id = db.Column(db.BIGINT, primary_key=True)

    # use the lowercased model class name as the __tablename__
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    def __init__(self, *args, **kwargs):
        for attr in (a for a in dir(self) if not a.startswith('_')):
            attr_obj = getattr(self, attr)
            if isinstance(attr_obj, db.Column):
                if attr in kwargs:
                    setattr(self, attr, kwargs[attr])
                else:
                    if hasattr(attr_obj, 'default'):
                        if callable(attr_obj.default):
                            setattr(self, attr, attr_obj.default())
                        else:
                            setattr(self, attr, attr_obj.default)


class DataMappingConfigs(db.Model, AutoInitMixin):
    domain = db.Column(db.String(32), index=True, unique=True)
    created_at = db.Column(db.TIMESTAMP, server_default=func.now())
    config = db.Column(JSON(none_as_null=True))


class TasksRuns(db.Model, AutoInitMixin):
    created_at = db.Column(db.TIMESTAMP, server_default=func.now())
    status = db.Column(db.Boolean, default=False)
