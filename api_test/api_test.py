# coding=utf-8

__author__ = 'Administrator'

import cof.http as cofHttp

# 数据分析API
api = 'api.data.91open.com'
port = 80

http_obj = cofHttp.Http(api, port)

print http_obj.get("/syslog")
