# coding = utf-8
__author__ = 'donglin'

from flask import Flask

from flask.ext.script import Manager

from flask.ext.mail import Message

from flask.ext.mail import Mail

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


@app.route('/')
def index():
    msg = Message("test subject", sender="hong2516@163.com", recipients=["cleardo@yeah.net"])

    msg.body = "text body"
    msg.html = "<b>bold</b> body"

    mail.send(msg)

    return "hello"


if __name__ == "__main__":
    app.run(debug=True)
