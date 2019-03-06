from flask import Flask, request, render_template, flash
from controller.jublia import JubliaController
from forms.email import EmailForm

app = Flask(__name__)
app.secret_key = b'MzgSuSc4yGm7zTx'


@app.route('/save_emails', methods=['GET', 'POST'])
def save_emails():
    form = EmailForm(request.form)
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
        return render_template('save_emails.html', form=EmailForm())
    else:
        return render_template('save_emails.html', form=form)


jublia = JubliaController()

app.run('0.0.0.0', '9000')
