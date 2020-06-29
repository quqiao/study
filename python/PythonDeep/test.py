#coding=utf-8
'''
Created on 2016年9月13日

@author: quqiao
'''

import sys
def readfile(filename):
    f=file(filename)
while True:
    line=f.readline()
if len(line)==0:
    break
print line
f.close()
