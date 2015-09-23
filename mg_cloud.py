# coding=utf-8

__author__ = 'Administrator'

import pymongo

connection = pymongo.Connection('192.168.9.105', 27317)

db = connection.cloud

coll = db.oa_accessgrant

tok = coll.find_one({"ClientId": 12})

print "token: ", tok["_id"]

print tok["RefreshToken"]


def get_hy_token():
    pass


from hy_grant import *

mg_conn = MongodbConn('192.168.9.105', 27317)
mg_conn.set_coll("cloud", "oa_accessgrant")
print mg_conn.find_one({"ClientId": 12})

grant_mg_conn = GrantMongodb('192.168.9.105', 27317)
grant_mg_conn.set_coll("cloud", "oa_accessgrant")
print grant_mg_conn.find_one({"ClientId": 12})
print "获取的access token: ", grant_mg_conn.get_token()

