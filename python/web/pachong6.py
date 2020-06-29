#coding=utf-8
'''
Created on 2016年6月13日

@author: quqiao
math的方法和属性
'''

import re
# 匹配如下内容：单词+空格+单词+任意字符
m=re.match(r'(\w+) (\w+)(\S+)', 'hello world!')

print "m.string:",m.string
print "m.re:",m.re
print "m.pos:",m.pos
print "m.endpos:",m.endpos
print "m.lastindex:",m.lastindex
print "m.lastgroup:",m.lastgroup
print "m.groups()",m.groups()
print "m.group(1,2,3):",m.group(1,2,3)
print "m.groupdict():",m.groupdict()
print "m.start(2):",m.start(2)
print "m.end():",m.end(2)
print "m.span(2):",m.span(2)
print "m.expand（r'\g \g\g'):",m.expand(r'\3 \2\1')
