from flask import Flask

from .routes import blue_print


def create_app():
    app = Flask(__name__)
    app.register_blueprint(blue_print)

    return app
