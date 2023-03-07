from flask import Blueprint, redirect, render_template, request, url_for
from .database import DataBase, TrainType
from config import Config
from forms.trains import AddForm

routes = Blueprint("routes", __name__, url_prefix="/", template_folder="templates")


@routes.route("/", methods=["GET"])
def index():
    """
    renders the index page

    :return: rendered template
    """
    db = DataBase(Config.DATABASE)
    locomotives = db.get_all_trains(train_type=TrainType.LOCOMOTIVE)
    wagons = db.get_all_trains(train_type=TrainType.WAGON)
    return render_template("index.html", locomotives=locomotives, wagons=wagons)


@routes.route("/overview", methods=["GET"])
def overview():
    """
    renders the overview template and inserts a list of all trains

    :return: rendered template
    """

    raise NotImplemented


@routes.route("/add", methods=["GET", "POST"])
def add():
    """
    renders the add page or handels submited data

    :return:rendered template or redirect to index
    """
    form = AddForm()
    if request.method == "POST" and form.validate():
        data = form.data
        del data["csrf_token"]
        data["train_type"] = TrainType[data["train_type"]]

        db = DataBase(Config.DATABASE)
        db.add_train(**data)
        db.close()

        return redirect(url_for("routes.index"))

    return render_template("add.html", form=form)
