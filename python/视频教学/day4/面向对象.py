#coding=utf-8
'''
Created on 2016年12月9日

@author: quqiao
'''

class Province(object):
    
    #静态字段
    memo='中国的23个省之一'
    
    def __init__(self,name,capital,leader,flag):
        #动态字段
        self.Name=name
        self.Capital=capital
        self.Leader=leader
        self.__Thailand = flag  #私有字段
     
    #动态方法   
    def sports_meet(self):
        print self.Name + '正在开运动会'
    
    #静态方法   
    @staticmethod
    def Foo():
        print '每个省都带头反复'
        
    
    #特性
    @property
    def Bar(self):
        print self.Name
    
      
    def show(self):
        print self.__Thailand
        
    
    #私有方法
    def __sha(self):
        print "私有方法"
        
    def foo2(self):
        self.__sha()
    
    #只读    
    @property
    def Thailand(self):
        return self.__Thailand
    
    
    #只写
    @Thailand.setter
    def Thailand(self,value):
        self.__Thailand=value
        
    
    
#sc=Province('四川','成都','lx',True)  #实例化对象
#print sc.Name     #访问动态字段
#sc.sports_meet()  #访问动态方法
#sc.Bar            #访问特性
#Province.Foo()    #访问静态方法
#print Province.memo     #访问静态字段
#sc.show()         #访问私有字段
#sc.foo2()         #访问私有方法
#print sc.Thailand       #访问私有字段
#sc._Province__sha()     #直接访问私有方法

#print sc.Thailand   #修改前打印
#sc.Thailand=False   #可写后修改
#print sc.Thailand   #修改后打印


class Foo():
    def __init__(self):
        print'初始化'     #pass
    
    def __del__(self):
        print '解释器要销毁我了，我要做最后一次的呐喊！'
        
    def Go(self):
        print 'Go!'
        
    def __call__(self):
        print 'call方法'
        
f1=Foo()  #执行类的__init__方法
#f1.Go()  #执行Go函数
#f1()      #执行类的__call__方法




