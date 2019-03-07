from wtforms import Form, SelectField


class EmailEventForm(Form):
    event_id = SelectField('Event ID', coerce=int)
    email_id = SelectField('Event ID', coerce=int)
