#coding=utf-8
'''
Created on 2016年12月12日

@author: quqiao
'''

#基类或者父类
class Father(object):
    def __init__(self):
        self.Fname='ffff'
        print 'father.__init__'
              
    def Func(self):
        print 'father.func'    
    def Bad(self):
        print 'father.抽烟喝酒烫头'

#派生类或者子类       
class Son(Father):
    def __init__(self):
        self.Sname='ssss' 
        print 'son.__init__'  #子类
        #Father.__init__(self) #调用父类
        super(Son,self).__init__() #调用父类
           
    def Bar(self):
        print 'son.bar'  
    '''  
    #重写父类bad方法
    def Bad(self):
        print 'son.抽烟喝酒'
    '''
    def Bad(self):
        Father.Bad(self)
        print 'son.赌博'

s2=Father()
s2.Func()
#s1=Son()
#s1.Bar()
#s1.Func()
#s1.Bad()


#新式类 ： object, C接口，新式类兼容经典类

#经典类：
