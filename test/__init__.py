from app import Flask, create_app
from config import TestingConfig

app: Flask = create_app(TestingConfig)
