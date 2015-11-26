# coding=utf-8

from nd.rest.http import Http

host = "plot.qa.sdp.nd"

http_o = Http(host)
res = http_o.get("/api_get.json")

print res

