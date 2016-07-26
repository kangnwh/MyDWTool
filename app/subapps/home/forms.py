from flask_wtf import Form
from wtforms import TextField,BooleanField,PasswordField
from wtforms.validators import DataRequired, ValidationError

class LoginForm(Form):
    email = TextField('ID', validators = [DataRequired()])
    password = PasswordField('password', validators = [DataRequired()])
    remember_me = BooleanField('remember_me', default = False)