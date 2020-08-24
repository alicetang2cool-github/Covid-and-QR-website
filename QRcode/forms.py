from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class StringForm(FlaskForm):
    string = StringField('String', validators=[DataRequired(), Length(min=1, max=100)])
    submit = SubmitField('make QRcode')

class PasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(), Length(min=1, max=100)])
    submit = SubmitField('make QRcode')