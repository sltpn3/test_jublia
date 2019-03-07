from flask import Flask, request, render_template, flash
from controller.jublia import JubliaController
from forms.email_to_send import EmailToSendForm
from forms.email import EmailForm
from forms.event import EventForm

app = Flask(__name__)
app.secret_key = b'MzgSuSc4yGm7zTx'


@app.route('/save_emails', methods=['GET', 'POST'])
def save_emails():
    form = EmailToSendForm(request.form)
    form.event_id.choices = jublia.event_id_choices()
    if request.method == 'POST' and form.validate():
        event_id = request.form.get('event_id', None)
        email_subject = request.form.get('email_subject', None)
        email_content = request.form.get('email_content', None)
        timestamp = request.form.get('timestamp', None)
        try:
            jublia.post_save_emails(event_id, email_subject, email_content, timestamp)
            flash('Data Saved')
        except Exception, e:
            '''Usually we send it to error tracking tool such as sentry'''
            print e
            flash('Error Saving Data')
        return render_template('save_emails.html', form=form)
    else:
        return render_template('save_emails.html', form=form)


@app.route('/emails', methods=['GET', 'POST'])
def emails():
    form = EmailForm(request.form)
    if request.method == 'POST' and form.validate():
        email_address = request.form.get('email')
        try:
            jublia.post_emails(email_address)
            flash('Data Saved')
        except Exception, e:
            print e
            flash('Error Saving Data')
        return render_template('emails.html', form=form)
    else:
        return render_template('emails.html', form=form)


@app.route('/events', methods=['GET', 'POST'])
def events():
    form = EventForm(request.form)
    if request.method == 'POST' and form.validate():
        event_name = request.form.get('event_name')
        try:
            jublia.post_events(event_name)
            flash('Data Saved')
        except Exception, e:
            print e
            flash('Error Saving Data')
        return render_template('events.html', form=form)
    else:
        return render_template('events.html', form=form)

jublia = JubliaController()

app.run('0.0.0.0', '9000')
