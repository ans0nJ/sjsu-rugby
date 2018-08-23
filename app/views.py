from flask import Flask, flash, g, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from flask_wtf import CSRFProtect

from app import app
from app.config import MAIL_PASSWORD, MAIL_USERNAME, RECIPIENT
from app.forms import ContactForm
from app.models import Contact, Roster, Schedule

mail = Mail()

app.secret_key = 'development key'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = MAIL_USERNAME
app.config["MAIL_PASSWORD"] = MAIL_PASSWORD


@app.route("/", methods=('GET', 'POST'))
def index():
    schedule = Schedule.query.all()
    roster = Roster.query.order_by('name').all()
    
    mail.init_app(app)

    form = ContactForm(request.form)

    if request.method == 'POST' and form.validate():
        msg = Message("Message from " + form.name.data, sender=MAIL_USERNAME, recipients=[MAIL_USERNAME])
        msg.body = """
        From: %s <%s>
        %s
        """ % (form.name.data, form.email.data, form.message.data)
        mail.send(msg)
        return redirect(url_for("index"))

    return render_template("index.html", schedule=schedule, roster=roster, form=form)
