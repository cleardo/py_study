# coding=utf-8
import mysql
from mysql.connector import fabric
from mysql.connector.fabric import Fabric

__author__ = 'linzh'


"""
测试mysql fabric

mysql-connector 只支持1.2.3版本
"""

fabric_config={
           "host": "qa1.rds.sdp.nd",
           "port": 32271,
           "username": "admin",
           "password" : "ZB5dGGTJtsC8t7O",
}

fabinst = Fabric(fabric_config)

config = {
    "fabric":
        {
        "host": "qa1.rds.sdp.nd",
        "port": 32271,
        "user": "admin",
        "password" : "ZB5dGGTJtsC8t7OQ",
    },
    "user":"user_n5s6dzrlcu",
    "password":"fzYbIUDTcE",
    "autocommit": True,
    "database": "qa_mysql_waf_demo_db"
}

conn = mysql.connector.connect(**config)
# conn.set_property(group="my_group_3307", mode=fabric.MODE_READWRITE)
conn.set_property(group="my_group_3307", mode=fabric.MODE_READONLY)

cur = conn.cursor()

cur.execute("select * from zipkin")

for row in cur:
    print row

exit()

config = {
    "fabric":fabinst,
    "user":"user_n5s6dzrlcu",
    "password":"fzYbIUDTcE",
    "autocommit": True,
    "database": "qa_mysql_waf_demo_db"
}


config2 = {
    "host": "192.168.19.97",
    "port": 3306,
    "user": "cleardo",
    "password": "lifeadmin",
    "database": "lzh_blog"
}

config3 = {
        "fabric": {
        'host': 'qa1.rds.sdp.nd',
        'port': 32271,
        "user": "admin",
        "password": "ZB5dGGTJtsC8t7O"
       }
}

# conn = mysql.connector.connect(**config3)

conn = fabric.MySQLFabricConnection(**config3)

conn.set_property(group="my_group_3307", mode=fabric.MODE_READONLY)

cur = conn.cursor()

# cur.execute("SELECT * FROM zipkin")


