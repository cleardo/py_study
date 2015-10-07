# coding=utf-8

__author__ = 'donglin'


from flask import Flask
# 引入flask restful框架
from flask_restful import Resource, Api


app = Flask(__name__)

api = Api(app)

# 资源
# 定义资源的GET操作
class HelloWorld(Resource):
    def get(self):
        # 从数据库获取数据，然后填充dict
        return {"hello": "world"}

# 对资源定义'/'
api.add_resource(HelloWorld, '/')

if __name__ == "__main__":
    app.run(debug=True)
