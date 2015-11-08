# coding=utf-8

__author__ = 'donglin'


from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap

import jinja2_highlight

class MyFlask(Flask):
    jinja_options = dict(Flask.jinja_options)
    jinja_options.setdefault('extensions', []).append('jinja2_highlight.HighlightExtension')

app = MyFlask(__name__)

bootstrap = Bootstrap(app)


@app.route("/")
def index():
    return render_template("client/index.html")


@app.route("/table")
def table():
    return render_template("client/table.html")


@app.route('/highlight')
def hl():
    return render_template("client/highlight.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
