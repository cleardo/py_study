# coding=utf-8

import time
import urllib

import cof.http as cofHttp
import cof.mysql as cofMysql

from hy_grant import *

grant_mg_conn = GrantMongodb('192.168.9.105', 27317)
grant_mg_conn.set_coll("cloud", "oa_accessgrant")
print grant_mg_conn.find_one({"ClientId": 12})

tok = grant_mg_conn.get_token()
http_obj = cofHttp.Http('api.data.91open.com', 80)

# tok = "91382970248e4aadb286036451424a43"
# httpobj = cofHttp.Http('test.metis.huayu.nd', 8881)

print "获取的access token: ", tok

header = {
    "Content-Type": "application/x-www-form-urlencoded",
    "AccessToken": tok
}

http_obj.set_header(header)

# print http_obj.get("/")

ts = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())

post_data = dict()
post_data["LogLevel"] = 2
post_data["LogMessage"] = "QA3_LogMessage2"
post_data["LogCallStack"] = "QA3_LogCallStack1"
post_data["CallTimestamp"] = ts

print post_data

params = urllib.urlencode(post_data)

res = http_obj.post("/syslog", params)
print "响应：%s" % res['data']

# 进行数据库比对验证
conn = cofMysql.MysqlConn("192.168.9.105", 3306)
conn.set_db_cfg_type('production')
conn.set_db_cfg()

params = dict()

table = 'syslog_log_type'
conn.set_table(table)

sql = "SELECT * FROM " + table + "\
       WHERE LogMessage = '%s' LIMIT 0, 100" % post_data['LogMessage']

print conn.exec_sql(sql)
print "异常消息：", post_data['LogMessage']
print "查询条数：", conn.count()
if not conn.count():
    print "异常消息丢失！"

table = 'syslog_detail_data'
conn.set_table('syslog_detail_data')
sql = "SELECT * FROM " + table + "\
       WHERE TypeId = '%d' LIMIT 0, 100" % 7

print conn.exec_sql(sql)
conn.close()
