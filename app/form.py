from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, TextAreaField, SelectField, IntegerField, RadioField
from wtforms.validators import InputRequired
from models import Profile
from flask_wtf.file import FileAllowed


class RegisterForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    firstname = StringField('firstname', validators=[InputRequired()])
    lastname = StringField('lastname', validators=[InputRequired()])
    sex = RadioField('gender', choices = [('M','Male'),('F','Female')])
    age = IntegerField('age', validators=[InputRequired()])
    pic = FileField('pic', validators=[FileAllowed(['png', 'jpg', 'jpeg', 'gif'], 'Images only!')])
    
    
    
class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])