#coding=utf-8


#经典类
'''
class A():
    def __init__(self):
        pass
    def save(self):
        print "This is from A"
class B(A):
    def __init__(self):
        pass
class C(A):
    def __init__(self):
        pass
    def save(self):
        print  "This is from C"
class D(B,C):
    def __init__(self):
        pass
fun =  D()
fun.save()
'''


#新式类
'''
class A(object):
    def __init__(self):
        pass
    def save(self):
        print "This is from A"
class B(A):
    def __init__(self):
        pass
    def save(self):
        print "This is from B"
class C(A):
    def __init__(self):
        pass
    def save(self):
        print  "This is from C"
class D(B,C):
    def __init__(self):
        pass
fun =  D()
fun.save()
'''

#封装
'''
class Fish(object):
    __eyes = 2
    
    def get_eye(self):
        return self.__eyes
    
fish = Fish()
print fish.get_eye()
'''

#继承
'''
class Fish(object):
    def __init__(self):
        self.eye=2
        self.wb=1
        

    def swam(self):
        print "我会游泳"


class GoldFish(Fish):
    def __init__(self):
        super(GoldFish,self).__init__()
        self.wb = 3
        self.cc="hello"

gold = GoldFish()
print gold.eye
print gold.wb
print gold.cc
gold.swam()
'''

#多态
'''
class Ball:
    def setName(self,name):
        self.name = name
    
    def kick(self):
        print "我叫%s，该死的，谁踢我..." % self.name
        
a = Ball()
a.setName("球A")
# 第一个参数self告诉Python是a对象在调用方法，因为是隐藏的并且由Python自己传入，所以我们这里不需要写进来。
b = Ball()
b.setName('球B')

c = Ball()
c.setName('球C')

a.kick()
b.kick()
c.kick()
'''

#组合
'''
class Turtle:
    def __init__(self,x):
        self.num = x
        
class Fish:
    def __init__(self,y):
        self.num = y

class Pool:
    def __init__(self,x,y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)
        
    def print_num(self):
        print "水池里总共有乌龟 %d 只，小鱼 %d 条！" % (self.turtle.num, self.fish.num)
'''

import time

class Fish(object):
    def __del__(self):
        print("我被销毁了")

fish1 = Fish()
a = fish1
b = fish1
#del b
#del a
#del fish1
time.sleep(1)
