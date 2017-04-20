from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, TextAreaField, SelectField, IntegerField, RadioField
from wtforms.validators import InputRequired, Email
from models import Profile
from flask_wtf.file import FileAllowed


class RegisterForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    firstname = StringField('firstname', validators=[InputRequired()])
    lastname = StringField('lastname', validators=[InputRequired()])
    email = StringField('email', validators=[InputRequired(), Email()])
    gender = RadioField('gender', choices = [('M','Male'),('F','Female')])
    password = PasswordField('password', validators=[InputRequired()])

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    
class WishForm(FlaskForm):
    title = StringField('title', validators=[InputRequired()])
    description = TextAreaField('description', validators=[InputRequired()])
    url = StringField('', validators=[InputRequired()])