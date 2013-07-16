from wtforms import Form, TextField, PasswordField, BooleanField
from wtforms.validators import Required, Email, EqualTo

class LoginForm(Form):
    email = TextField('Email Address', [Required(), Email()])
    password = PasswordField('Password', [Required()])

class RegisterForm(Form):
    name = TextField('NickName', [Required()])
    email = TextField('Email Address', [Required(), Email()])
    password = PasswordField('Password', [Required()])
    confirm = PasswordField('Repeat Password', [
        Required(),
        EqualTo('password', message='Passwords must match')
        ])
    accept_tos = BooleanField('I access the TOS')
