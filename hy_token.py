# coding=utf-8
__author__ = 'Administrator'

import httplib

url = "/v1/oauth/token?client_id=1&client_secret=DB3CFF12016348AAB9834D284D8093D7&username=1012725687%40qq.com&password=ae76d37167c52111351469a677b0a995&grant_type=password&account_type=user_center&access_token=&platcode=800110010000"

conn = httplib.HTTPConnection('test.cloud.91open.huayu.nd')
conn.request(method="GET", url=url)
response = conn.getresponse()

print response.status
print response.read()

if response.status != 200:
    print response.status
    print response.read()
    conn.close()
    exit()

conn.close()