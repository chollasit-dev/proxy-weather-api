import pytest
from flask import Response
from markupsafe import escape

from app.sample.routes import index, try_escaping_script
from test import app


def test_index() -> None:
    with app.test_request_context():
        response: Response = index()
        assert response.status_code == 200


test_script: str = "<script>alert('test')</script>"


@pytest.mark.parametrize(
    "script, escaping, expected",
    [
        (test_script, "True", escape(test_script)),
        (test_script, "true", escape(test_script)),
        (test_script, "yes", escape(test_script)),
        (test_script, "1", escape(test_script)),
        (test_script, "False", test_script),
        (test_script, "false", test_script),
        (test_script, "no", test_script),
        (test_script, "0", test_script),
    ],
)
def test_try_escaping_script(script: str, escaping: str, expected: str) -> None:
    with app.test_request_context(
        query_string={"script": script, "escaping": escaping}
    ):
        response: Response = try_escaping_script()
        assert response.get_data(as_text=True) == expected
