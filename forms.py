from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, NumberRange, Optional, URL

class AddCupcakeForm(FlaskForm):
    flavor = StringField("Cupcake Flavor:", validators=[InputRequired(message="Please enter a flavor")])
    size = SelectField("Cupcake Size:", choices=[
                                                ('sm', 'small'), ('m', 'medium'), ('lg', 'large')])
    rating = FloatField("Taste Rating 1-10:", validators=[NumberRange(min=1, max=10), InputRequired(message="Please enter a rating")])
    image = StringField("Enter a Photo URL:", validators=[Optional()])