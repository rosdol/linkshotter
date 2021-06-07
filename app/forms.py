from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

class ShortedLinkForm(FlaskForm):
    long_url = StringField('URL', validators=[DataRequired(), URL()])
    token = StringField('Custom URL (optional)')
    submit = SubmitField('Shorten')
