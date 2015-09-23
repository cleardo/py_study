__author__ = 'Administrator'

import zipfile
import cof.http as cofHttp

api = 'api.data.91open.com'
port = 80

http_obj = cofHttp.Http(api, port)

print http_obj.get("/syslog")
