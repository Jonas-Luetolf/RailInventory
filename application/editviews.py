from flask import Blueprint, redirect, render_template, url_for, request
from forms import trains
from .database import DataBase, TrainType
from config import Config

edit_views = Blueprint(
    "edit_views", __name__, url_prefix="/edit/", template_folder="templates"
)


@edit_views.route("/locomotive", methods=["GET", "POST"])
def locomotive():
    form = trains.LocomotiveForm()
    db = DataBase(Config.DATABASE)

    if request.method == "POST" and form.validate():
        data = form.data
        del data["csrf_token"]
        train_type = TrainType.LOCOMOTIVE
        db.update_train(train_type, **data)
        db.close()
        return redirect(url_for("views.index"))

    else:
        form = trains.LocomotiveForm(
            data=db.get_train_by_id(TrainType.LOCOMOTIVE, request.args.get("id"))
        )
        return render_template("locomotive.html", form=form, action="/edit/locomotive")


@edit_views.route("/wagon", methods=["GET", "POST"])
def wagon():
    form = trains.WagonForm()
    db = DataBase(Config.DATABASE)

    if request.method == "POST" and form.validate():
        data = form.data
        del data["csrf_token"]
        train_type = TrainType.WAGON
        db.update_train(train_type, **data)
        db.close()
        return redirect(url_for("views.index"))

    else:
        form = trains.WagonForm(
            data=db.get_train_by_id(TrainType.WAGON, request.args.get("id"))
        )
    return render_template("wagon.html", form=form, action="/edit/wagon")
