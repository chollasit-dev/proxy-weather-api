from flask import Flask

from config import DevelopmentConfig, ProfileOption


def create_app(
    config: ProfileOption = DevelopmentConfig,
) -> Flask:
    app: Flask = Flask(__name__)
    app.config.from_object(config)

    app.url_map.strict_slashes = False

    from app.sample.routes import bp as sample_bp

    app.register_blueprint(sample_bp)

    return app
