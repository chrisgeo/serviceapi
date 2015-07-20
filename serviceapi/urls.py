
from serviceapi.resources.main import main, index
from serviceapi.resources.api_vone import api_vone

routes = [
    (
        (main, ''),
        ('/', index),
    ),
    (api_vone)
]
