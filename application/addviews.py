from flask import Blueprint, redirect, render_template, url_for, request, current_app
from forms import trains
from .database import DataBase, TrainType

add_views = Blueprint(
    "add_views", __name__, url_prefix="/add/", template_folder="templates"
)


def add_train(train_type: TrainType, data: dict) -> None:
    del data["id"]
    if "csrf_token" in data:
        del data["csrf_token"]
    db = DataBase(current_app.config["DATABASE"])
    db.add_train(train_type, **data)
    db.close()


@add_views.route("/locomotive", methods=["GET", "POST"])
def locomotive():
    form = trains.LocomotiveForm()
    if request.method == "POST" and form.validate():
        add_train(TrainType.LOCOMOTIVE, form.data)
        return redirect(url_for("views.index"))

    return render_template("locomotive.html", form=form, action="/add/locomotive")


@add_views.route("/wagon", methods=["GET", "POST"])
def wagon():
    form = trains.WagonForm()
    if request.method == "POST" and form.validate():
        add_train(TrainType.WAGON, form.data)
        return redirect(url_for("views.index"))

    return render_template("wagon.html", form=form, action="/add/wagon")
