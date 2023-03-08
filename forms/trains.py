from wtforms import (
    IntegerField,
    SelectField,
    StringField,
    TextAreaField,
    validators,
)
from flask_wtf import FlaskForm


class AddForm(FlaskForm):
    train_type = SelectField(
        "train_type", choices=[("LOCOMOTIVE", "Lokomotive"), ("WAGON", "Wagon")]
    )
    name = StringField("name", validators=[validators.InputRequired()])
    number = IntegerField(
        "numbers",
        validators=[
            validators.InputRequired(),
            validators.NumberRange(min=0, message="Nummer muss grösser als 0 sein"),
        ],
    )
    producer = StringField("producer", validators=[validators.InputRequired()])
    comment = TextAreaField("comment", validators=[validators.InputRequired()])
