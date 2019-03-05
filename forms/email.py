from wtforms import Form, StringField, IntegerField, TextAreaField
from wtforms.fields.html5 import DateTimeLocalField


class EmailForm(Form):
    event_id = IntegerField('Event ID')
    email_subject = StringField('Email Subject')
    email_content = TextAreaField('Email Content')
    timestamp = DateTimeLocalField('Time To Send ', format='%Y-%m-%dT%H:%M')
