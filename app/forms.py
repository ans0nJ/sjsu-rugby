from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, TextAreaField, TextField
from wtforms.validators import Required


class ContactForm(FlaskForm):
    name = TextField("name", [Required("Please enter your name.")])
    email = TextField("email", [Required("Please enter your email.")])
    message = TextAreaField("message")
    submit = SubmitField("send message")
