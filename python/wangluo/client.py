#coding=utf-8
'''
Created on 2016年8月19日

@author: quqiao
'''


import socket

s=socket.socket()
host=socket.gethostname()
port=12345

s.connect((host,port))
print s.recv(1024)
s.close()

