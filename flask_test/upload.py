# -*- coding: UTF-8 -*-
import os
import datetime

from cross import crossdomain

from tornado.escape import *

from flask.ext.wtf import Form
from werkzeug.utils import secure_filename
from wtforms import StringField, FileField, SubmitField

__author__ = 'donglin'

from flask import Flask, render_template, request, Response

from flask.ext.script import Manager

from flask.ext.mail import Message

from flask.ext.mail import Mail

from flask.ext.bootstrap import Bootstrap

from flask.ext.moment import Moment


class MyFlask(Flask):
    jinja_options = dict(Flask.jinja_options)
    jinja_options.setdefault('extensions', []).append('jinja2_highlight.HighlightExtension')


app = MyFlask(__name__)

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
moment = Moment(app)

from flask.ext.cors import CORS

# cors = CORS(app, resources={r"/jsonp": {"origins": "*"}, r"/upload": {"origins": "*"}})

class UploadForm(Form):
    name = StringField("file")
    up_file = FileField(u"上传")
    submit = SubmitField(u"提交")

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadForm()

    return render_template("upload.html", current_time=datetime.datetime.utcnow(), form=form)

@app.route("/jsonp2")
def jsonp():
    args = request.args
    print args
    func_name = args["callbackparam"]

    retn = {"data": [["value"], ["value2"]]}
    retn = func_name + '(' + json_encode(retn) + ')'
    resp = Response(retn, status=200, mimetype="application/json")
    return resp

@app.route('/jsonp_table')
def jsonp_table():
    args = request.args

    print args

    func_name = args["callback"]

    retn = {"data": [["value", "row1.col2"], ["value2", "row2.col2"]]}
    retn = func_name + '(' + json_encode(retn) + ')'
    resp = Response(retn, status=200, mimetype="application/json")
    return resp


@app.route('/cross', methods=['GET', 'POST'])
def cross():
    """
    跨域

    :return:
    """
    return render_template("cross.html")

@app.route('/chosen', methods=['GET', 'POST'])
def chosen():
    return render_template("chosen.html")

@app.route('/steps', methods=['GET', 'POST'])
def step():
    return render_template("steps.html"), 200


@app.route('/jsonp', methods=['GET', 'POST', 'OPTIONS'])
@crossdomain(origin='*', methods=['OPTIONS'])
def jsonp_test():
    print request.form
    return "jsonp"
    # print request.data
    # post_data = json_decode(request.data)
    # return json_encode({"key": post_data.get('key')}), 200, {'Access-Control-Allow-Origin': 'http://127.0.0.1:5001'}

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    # view中调用wtf.quick_form()
    form = UploadForm()

    print request.files

    if request.method == 'GET':
        return render_template("client/upl.html", form=form)

    f = request.files['file']
    filename = secure_filename(f.filename)
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    if form.validate_on_submit():
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print "ok"

    return "", 200, {'Access-Control-Allow-Origin': '*'}
    # render_template()

@app.route('/mail')
def mail():
    msg = Message("test subject", sender="hong2516@163.com", recipients=["cleardo@yeah.net"])

    msg.body = "text body"
    msg.html = "<b>bold</b> body"

    mail.send(msg)

    return "hello"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
