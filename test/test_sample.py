from flask import Response

from app.sample.routes import index
from test import app


def test_index() -> None:
    with app.test_request_context():
        response: Response = index()
        assert response.status_code == 200
