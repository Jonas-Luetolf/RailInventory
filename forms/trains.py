from wtforms import (
    HiddenField,
    IntegerField,
    SelectField,
    StringField,
    TextAreaField,
    validators,
    widgets,
)
from flask_wtf import FlaskForm


class WagonForm(FlaskForm):
    id = IntegerField(
        default=0,
        validators=[validators.NumberRange(min=0), validators.Optional()],
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


class LocomotiveForm(FlaskForm):
    id = IntegerField(
        validators=[validators.NumberRange(min=0), validators.Optional()], default=0
    )
    name = StringField("name", validators=[validators.InputRequired()])
    number = IntegerField(
        "numbers",
        validators=[
            validators.InputRequired(),
            validators.NumberRange(min=0, message="Nummer muss grösser als 0 sein"),
        ],
    )

    address = IntegerField(
        "address",
        validators=[
            validators.InputRequired(),
            validators.NumberRange(min=0, message="Addrese muss grösser als 0 sein"),
        ],
    )

    protocol = StringField("protocol", validators=[validators.InputRequired()])
    sound = IntegerField(
        "sound",
        validators=[
            validators.InputRequired(),
            validators.NumberRange(min=0, max=1, message="muss 1 oder 0 sein"),
        ],
    )

    ltype = StringField("ltype", validators=[validators.InputRequired()])
    vmax = IntegerField(
        "vmax",
        validators=[
            validators.InputRequired(),
            validators.NumberRange(
                min=0, message="Geschwindigkeit muss grösser als 0 sein"
            ),
        ],
    )
    power = IntegerField(
        "power",
        validators=[
            validators.InputRequired(),
            validators.NumberRange(min=0, message="Leistung muss grösser als 0 sein"),
        ],
    )
    year = IntegerField(
        "year",
        validators=[
            validators.InputRequired(),
            validators.NumberRange(min=0, message="Baujahr muss grösser als 0 sein"),
        ],
    )

    modelproducer = StringField("producer", validators=[validators.InputRequired()])
    producer = StringField("producer", validators=[validators.InputRequired()])
    comment = TextAreaField("comment", validators=[validators.InputRequired()])
