# coding=utf-8

__author__ = 'donglin'


import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(("127.0.0.1", 8888))

sock.send("GET / HTTP/1.1\n")
sock.send("User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:19.0) Gecko/20100101 Firefox/19.0")
sock.send("\r\n\r\n")

fp = open("../basic/test02.jpg", "rb")
pic_data = fp.read(100)
sock.send(pic_data)
fp.close()

print sock.recv(1024)

sock.close()
