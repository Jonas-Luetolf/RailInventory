from flask import Blueprint, redirect, render_template, url_for, request
from forms import trains
from .database import DataBase, TrainType
from config import Config

add_views = Blueprint(
    "add_views", __name__, url_prefix="/add/", template_folder="templates"
)


@add_views.route("/locomotive", methods=["GET", "POST"])
def locomotive():
    form = trains.LocomotiveForm()
    if request.method == "POST" and form.validate():
        data = form.data
        del data["csrf_token"]
        train_type = TrainType.LOCOMOTIVE
        db = DataBase(Config.DATABASE)
        db.add_train(train_type, **data)
        db.close()
        return redirect(url_for("views.index"))

    return render_template("addlocomotive.html", form=form)


@add_views.route("/wagon", methods=["GET", "POST"])
def wagon():
    form = trains.WagonForm()
    if request.method == "POST" and form.validate():
        data = form.data
        del data["csrf_token"]
        train_type = TrainType.WAGON
        db = DataBase(Config.DATABASE)
        db.add_train(train_type, **data)
        db.close()
        return redirect(url_for("views.index"))

    return render_template("addwagon.html", form=form)
