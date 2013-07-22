from wtforms import Form, TextField, PasswordField, BooleanField
from wtforms.validators import Required, Email, EqualTo

class LoginForm(Form):
    email = TextField('E-mail', [Required(), Email()])
    password = PasswordField('Password', [Required()])

class RegisterForm(Form):
    name = TextField('Name', [Required()])
    email = TextField('E-mail', [Required(), Email()])
    password = PasswordField('Password', [Required()])
    confirm = PasswordField('Repeat Password', [
        Required(),
        EqualTo('password', message='Passwords must match')
        ])
