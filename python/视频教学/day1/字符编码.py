#coding=utf-8
'''
Created on 2016年12月14日

@author: quqiao
'''

#assic码   存储1个字节
#unicode码  存储2个字节
#utf-8: 可变长度的编码   3个字节存一个汉字


name1='test'
name2=u'test'
name3=u'范特西'
#print type(name1)
#print type(name2)
#print name3
#print len(name3)
print name3.encode('utf-8')
#print type(name3)


