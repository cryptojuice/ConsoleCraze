from wtforms import Form, TextField, PasswordField, BooleanField, TextField,\
        TextAreaField
from wtforms.validators import Required, Email, EqualTo


class NewArticleForm(Form):
    title = TextField('Title', [Required()])
    content = TextAreaField('Summary', [Required()])
    url = TextField('Article Url', [Required()])
    image_url = TextField('Image Url')
