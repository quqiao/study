#coding=utf-8
'''
Created on 2016年12月13日

@author: quqiao
'''

str1 = 'demo'
str2 = 'Foo'

module = __import__(str1)
func = getattr(module, str2)


func()