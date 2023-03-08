from flask import Flask
from .views import views
from config import Config
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()


def create_app() -> Flask:
    """
    creates the flask app

    :return: Flask app
    """

    app = Flask("RailInventory", static_folder="application/static")
    app.config.from_object(Config)
    app.register_blueprint(views)
    csrf.init_app(app)
    return app
