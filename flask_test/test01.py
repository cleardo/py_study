# coding=utf-8
import time
import datetime

from flask.ext.restful import reqparse
import werkzeug

__author__ = 'donglin'


from flask import Flask, request
from flask_restful import Resource, fields, marshal_with

# 引入flask restful框架
from flask_restful import Resource, Api


app = Flask(__name__)

api = Api(app)

resource_fields = {
    'name': fields.String,
    'address': fields.String,
    'date_updated': fields.DateTime(dt_format='rfc822'),}

# 资源
# 定义资源的GET操作
class HelloWorld(Resource):
    @marshal_with(resource_fields, envelope='resource')
    def get(self):
        # 从数据库获取数据，然后填充dict
        return {"hello": "world", "date_updated": datetime.datetime.utcnow(), "address": 22}

    def post(self):
        # print request.get_json(force=True)
        parser = reqparse.RequestParser()

        # 表单提交
        parser.add_argument('rate', type=int, help='Rate cannot be converted')

        parser.add_argument('name')

        parser.add_argument('picture', type=werkzeug.datastructures.FileStorage, location='files')

        args = parser.parse_args()

        # 文件存储
        # args['picture']

        print args
        # print request.args
        print request.form['rate']

        # print request.data
        # print request.form
        # print request.args

        return {"hello": "world"}


# 对资源定义'/'
api.add_resource(HelloWorld, '/')

if __name__ == "__main__":
    app.run(debug=True)
