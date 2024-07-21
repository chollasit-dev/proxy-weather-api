from flask import Response, abort, make_response, request, url_for
from markupsafe import escape

from app.sample import bp


@bp.get("/")
def index() -> Response:
    content: str = """Welcome to basic proxy weather flask app test route!
    To get actual info, please send POST request to "/api/..." instead.
    """
    return make_response(content, 200)


@bp.get("/try_escaping_script")
def try_escaping_script() -> Response:
    script: str | None = request.args.get("script", None)
    if script is None:
        content: str = f"""No script parameter provide!
        To pass arguments, simply type arguments in the address bar
        "{url_for('try_escaping_script',
                  script='<script>any_script_here()</script>',
                  escaping='true_or_false')}"
        """
        return abort(400, content)

    escaping: str = request.args.get("escaping", "true")
    is_escaping: bool = False if escaping.lower() in ("false", "no", "0") else True

    return make_response(escape(script) if is_escaping else script, 200)
