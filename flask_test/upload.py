# -*- coding: UTF-8 -*-
import os

from flask.ext.wtf import Form
from werkzeug.utils import secure_filename
from wtforms import StringField, FileField, SubmitField

__author__ = 'donglin'

from flask import Flask, render_template, request

from flask.ext.script import Manager

from flask.ext.mail import Message

from flask.ext.mail import Mail

from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)

app.config['SECRET_KEY'] = "cleardoa*b(c%225588"

app.config['UPLOAD_FOLDER'] = "upload_data"

app.config['MAIL_SERVER'] = 'smtp.163.com'

app.config['MAIL_PORT'] = 25

# app.config['MAIL_USE_TLS'] = True

app.config['MAIL_USERNAME'] = "hong2516@163.com"

app.config['MAIL_PASSWORD'] = "2216593flik"

mail = Mail(app)
manager = Manager(app)
bootstrap = Bootstrap(app)

class UploadForm(Form):
    name = StringField("file")
    up_file = FileField(u"上传")
    submit = SubmitField(u"提交")

@app.route('/', methods=['GET', 'POST'])
def index():
    # view中调用wtf.quick_form()
    form = UploadForm()

    print request.files

    f = request.files['file']
    filename = secure_filename(f.filename)
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    if form.validate_on_submit():
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print "ok"

    # render_template()
    return render_template("upload.html", form=form)

@app.route('/mail')
def mail():
    msg = Message("test subject", sender="hong2516@163.com", recipients=["cleardo@yeah.net"])

    msg.body = "text body"
    msg.html = "<b>bold</b> body"

    mail.send(msg)

    return "hello"


if __name__ == "__main__":
    app.run(debug=True)
