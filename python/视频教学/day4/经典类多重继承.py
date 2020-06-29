#coding=utf-8
'''
Created on 2016年12月12日

@author: quqiao
'''


class A(object):
    def __init__(self):
        print "This is A"
        
    def save(self):
        print 'save method from A'
        
class B(A):
    def __init__(self):
        print 'This is B'
        
class C(A):
    def __init__(self):
        print 'This is C'
    def save(self):
        print 'save method form C'
        
class D(B,C):
    def __init__(self):
        print 'This is D'
        
d=D()
d.save()
        
    