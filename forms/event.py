from wtforms import Form, StringField
from wtforms import validators


class EventForm(Form):
    event_name = StringField('Event Name', [validators.DataRequired()])
