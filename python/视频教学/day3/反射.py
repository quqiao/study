#coding=utf-8

#import sqlserverhelper

#print sqlserverhelper.count()

#反射：以字符串的形式导入模块
'''
temp = 'sqlserverhelper'
model = __import__(temp)
model.count()
'''

#并以字符串形式执行函数
temp = 'mysqlhelper'
func = 'count'
model = __import__(temp)
Function = getattr(model,func)
print Function