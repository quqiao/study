#coding=utf-8
'''
Created on 2015年11月11日

@author: admin
'''
def func(a,b=5,c=10):
    print "a is",a,"and b is",b,"abd c is",c
func(3,7)
func(25,c=24)
func(c=50,a=100)
