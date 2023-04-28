from flask import Blueprint, redirect, render_template, request, url_for, current_app
from .database import DataBase, TrainType

views = Blueprint("views", __name__, url_prefix="/", template_folder="templates")


@views.route("/", methods=["GET"])
def index():
    """
    renders the index page

    :return: rendered template
    """
    db = DataBase(current_app.config["DATABASE"])
    locomotives = db.get_all_trains(train_type=TrainType.LOCOMOTIVE)
    wagons = db.get_all_trains(train_type=TrainType.WAGON)
    return render_template("index.html", locomotives=locomotives, wagons=wagons)
