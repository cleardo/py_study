# coding=utf-8
__author__ = 'Administrator'

import cof.mysql as cofMysql

conn = cofMysql.MysqlConn("192.168.9.105", 3306)
#conn.set_db_cfg_type('production')
conn.set_db_cfg()

params = dict()
params['ApiUrl'] = '/v1/oauth/valid'

table = 'apicall_statistics'
conn.set_table(table)

sql = "SELECT * FROM " + table + "\
       WHERE ApiUrl = '%s' LIMIT 0, 100" % params['ApiUrl']

print conn.exec_sql(sql)

conn.close()
