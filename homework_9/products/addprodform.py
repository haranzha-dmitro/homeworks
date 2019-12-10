from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, IntegerField, SubmitField
from wtforms.validators import DataRequired, InputRequired


class AddProductForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()])
    description = TextAreaField("Description: ", validators=[DataRequired()])
    img_name = FileField("Img_name: ")
    price = IntegerField("Price: ", validators=[DataRequired()])
    submit = SubmitField("Submit")