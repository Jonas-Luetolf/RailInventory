from flask import Flask
from .routes import routes


def create_app() -> Flask:
    """
    creates the flask app

    :return: Flask app
    """

    app = Flask("RailInventory", static_folder="application/static")
    app.register_blueprint(routes)

    return app
