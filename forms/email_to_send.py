from wtforms import Form, StringField, IntegerField, TextAreaField, SelectField
from wtforms.fields.html5 import DateTimeLocalField


class EmailToSendForm(Form):
#     event_id = IntegerField('Event ID')
    event_id = SelectField('Event ID', coerce=int)
    email_subject = StringField('Email Subject')
    email_content = TextAreaField('Email Content')
    timestamp = DateTimeLocalField('Time To Send ', format='%Y-%m-%dT%H:%M')
