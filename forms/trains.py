from wtforms import (
    Form,
    IntegerField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
    validators,
)
from flask_wtf import FlaskForm


class AddForm(FlaskForm):
    train_type = SelectField(
        "train_type", choices=[("LOCOMOTIVE", "Lokomotive"), ("WAGON", "Wagon")]
    )
    name = StringField("name", validators=[validators.InputRequired()])
    number = IntegerField("numbers", validators=[validators.InputRequired()])
    producer = StringField("producer", validators=[validators.InputRequired()])
    comment = TextAreaField("comment", validators=[validators.InputRequired()])
