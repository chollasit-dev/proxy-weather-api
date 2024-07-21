import os
from typing import TypeAlias

# load_dotenv(".env")   # optional


class Config:
    API_KEY: str = os.getenv("API_KEY", "")
    ENV: str = os.getenv("FLASK_ENV", "development")
    DEBUG: bool = os.getenv("FLASK_DEBUG", "false").lower() in ("true", "1")


class DevelopmentConfig(Config): ...


class TestingConfig(Config):
    ENV: str = os.getenv("FLASK_ENV", "testing")


class ProductionConfig(Config):
    ENV: str = os.getenv("FLASK_ENV", "production")
    DEBUG: bool = False


ProfileOption: TypeAlias = type[Config]
