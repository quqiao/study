#coding=utf-8
'''
Created on 2015年11月13日

@author: admin 
'''
class Person:
    def __init__(self,name):
        self.name=name
    def sayHi(self):
        print 'Hello,my name is',self.name
        
p=Person('Swaroop')
p.sayHi()
