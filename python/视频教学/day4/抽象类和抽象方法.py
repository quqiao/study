##coding=utf-8
'''
Created on 2016年12月13日

@author: quqiao
'''

from abc import ABCMeta,abstractmethod
#from _pyio import __metaclass__

class Alert:
    __metaclass__=ABCMeta
    
    @abstractmethod
    def send(self):
        pass
    
    #抽象类+抽象方法=接口（第二种接口，即：规范）

class weixin(Alert):
    def __init__(self):
        print '__init__'
        
    def send(self):
        print 'send.weixin'
        
        
f=weixin()
f.send()



