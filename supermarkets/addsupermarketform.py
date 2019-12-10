from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField
from wtforms.validators import DataRequired, InputRequired


class AddMarketForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()])
    location = StringField("Location: ", validators=[DataRequired()])
    img_name = FileField("Img_name: ", validators=[InputRequired()])
    submit = SubmitField("Submit")
