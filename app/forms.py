from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired
from wtforms import FileField
from flask_wtf.file import FileAllowed, FileRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class UploadForm(FlaskForm):
    file = FileField('File', validators=[
        FileRequired(),  # Ensure a file is uploaded
        FileAllowed(['jpg', 'png'], 'Only JPG and PNG files are allowed!')  # Restrict to image files
    ])