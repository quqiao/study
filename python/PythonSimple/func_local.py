#coding=utf-8
'''
Created on 2015年11月11日

@author: admin
'''
def func(x):
    print "x is",x
    x=2
    print "Changed local x to",x
    
x=50
func(x)
print "x is still",x
