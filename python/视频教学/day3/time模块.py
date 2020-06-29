#coding=utf-8

import time

#print time.time()   #时间戳
#print time.gmtime()  #时间结构化格式
#print time.strftime('%Y%m%d %H%M%S') #时间字符串的格式，默认当前时间

#print time.localtime()
print time.strptime('2014-11-11','%Y-%m-%d') #字符串转结构化
#print time.mktime(time.localtime())  #结构化转时间戳
