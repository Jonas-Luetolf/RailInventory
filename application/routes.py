from flask import Blueprint, redirect, render_template, request, url_for

routes = Blueprint("routes", __name__, url_prefix="/", template_folder="templates")


@routes.route("/", methods=["GET"])
def index():
    """
    renders the index page

    :return: rendered template
    """

    return render_template("index.html")


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

    if request.method == "GET":
        return render_template("add.html")

    else:
        return redirect(url_for("routes.index"))
