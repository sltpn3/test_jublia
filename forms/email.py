from wtforms import Form, StringField
from wtforms import validators


class EmailForm(Form):
    email = StringField('Email Address', [validators.DataRequired(), validators.Email()])
