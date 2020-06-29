#coding=utf-8
'''
Created on 2016年6月13日

@author: quqiao
re中的各种方法
'''

import re

#search方法
# 将正则表达式编译成Pattern对象
pattern=re.compile(r'world')
# 使用search()查找匹配的子串，不存在能匹配的子串时将返回None
# 这个例子中使用match()无法成功匹配
match=re.match(pattern, 'hello world!')
if match:
    print match.group()
else:
    print "failed"
    
#split方法
pattern=re.compile(r'\d+')
print re.split(pattern, 'one1two2three3four4')

#findall方法
pattern=re.compile(r'\d+')
print re.findall(pattern, 'one1two2three3four4')

#finditer方法
pattern=re.compile(r'\d+')
for m in re.finditer(pattern,'one1two2three3four4'):
    print m.group()
    
#sub方法
pattern=re.compile(r'(\w+)(\w+)') 
s='i say, hello world!'  

print re.sub(pattern, r'\2 \1', s)

def func(m):
    return m.group(1).title()+''+m.group(2).title()
print re.sub(pattern,func,s)

#subn方法
pattern=re.compile(r'(\w+) (\w+)')
s='i say, hello world!'

def func1(m):
    return m.group(1).title()+''+m.group(2).title()
print re.subn(pattern,func,s)




