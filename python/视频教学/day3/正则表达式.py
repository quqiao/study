#coding=utf-8



'''
#pattern  表达式
#string  字符串
#re.match 开头匹配 (只拿一个）
#re.search 整个字符串匹配（只拿一个）
#返回对象用group函数获取



result1 = re.match('\d+','s4dsfsdaf464afs6d4f6as')
result2 = re.search('\d+','s4dsfsdaf464afs6d4f6as')
if result1:   
    print result1.group()
else:
    print 'nothing'
print result2
print result2.group()
'''

'''
#re.findall 整个字符串匹配，全部取出
result3 = re.findall('\d+', 'asfd123sfds4asf567gtj89')
print result3
'''

'''
#re.compile
com = re.compile('\d+')
print type(com)
print com.findall('asfd123sfds4asf567gtj89')
'''

'''
#groups
result4 = re.search('(\d+)\w*(\d+)','asfd123sfds4asf567gtj89')
print result4.group()
print result4.groups()

#正则表达式常用格式： 
#\d  数字
#\w  下划线 
#\t  制表符
#.  除回车以为所有字符
#* 大于等于0
#+ 大于等于1
#?  0或1
#{m} 次数
#{m,n} 范围
'''


#匹配Ip地址


ip = '12.135.556.safasdf5.gasd.gsda..123sdg.fdggasd.192.168.32.43=+32-4rr2039#$$%%@##$'

import re

#print re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',ip)
print re.findall('(?:\d(1,3)\.){3}\d{1,3}',ip)


