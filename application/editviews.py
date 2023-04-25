from flask import Blueprint, redirect, render_template, url_for, request, current_app
from forms import trains
from .database import DataBase, TrainType


edit_views = Blueprint(
    "edit_views", __name__, url_prefix="/edit/", template_folder="templates"
)


def update_train(train_type: TrainType, data: dict) -> None:
    db = DataBase(current_app.config["DATABASE"])
    if "csrf_token" in data: del data["csrf_token"]
    db.update_train(train_type, **data)
    db.close()


@edit_views.route("/locomotive", methods=["GET", "POST"])
def locomotive():
    form = trains.LocomotiveForm()

    if request.method == "POST" and form.validate():
        update_train(TrainType.LOCOMOTIVE, form.data)
        return redirect(url_for("views.index"))

    else:
        db = DataBase(current_app.config["DATABASE"])
        form = trains.LocomotiveForm(
            data=db.get_train_by_id(TrainType.LOCOMOTIVE, request.args.get("id"))
        )
        return render_template("locomotive.html", form=form, action="/edit/locomotive")


@edit_views.route("/wagon", methods=["GET", "POST"])
def wagon():
    form = trains.WagonForm()

    if request.method == "POST" and form.validate():
        update_train(TrainType.WAGON, form.data)
        return redirect(url_for("views.index"))

    else:
        db = DataBase(current_app.config["DATABASE"])
        form = trains.WagonForm(
            data=db.get_train_by_id(TrainType.WAGON, request.args.get("id"))
        )
    return render_template("wagon.html", form=form, action="/edit/wagon")
