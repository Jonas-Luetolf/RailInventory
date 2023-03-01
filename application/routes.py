from flask import Blueprint, render_template

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

    :route: rendered template
    """

    raise NotImplemented

@routes.route("/add", methods=["GET","POST"])
def add():
    return render_template("add.html")
