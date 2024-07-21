from flask import Blueprint

bp: Blueprint = Blueprint(
    "sample",
    __name__,
    url_prefix="/sample/",
)

from app.sample import routes
