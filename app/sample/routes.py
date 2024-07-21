from flask import Response, make_response

from app.sample import bp


@bp.get("/")
def index() -> Response:
    content: str = """Welcome to basic proxy weather flask app test route!
    To get actual info, please send POST request to "/api/..." instead.
    """
    return make_response(content, 200)
