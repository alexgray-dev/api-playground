from flask import Flask

from .config import DevelopmentConfig
from .routes import bp


def create_app(config=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(bp)
    return app
