#coding=utf-8
'''
Created on 2016年12月15日

@author: quqiao
'''

#raw_input 默认输入字符串
#input   原生是什么类型就输入什么类型，不转换
#  %s 接受外面变量为字符串
#  %d 接受外面变量为数字
#  %f 接受外面变量为浮点数


name = raw_input("Please input your name:")
age  = raw_input('age:')
job  = raw_input('Job:')
salary = raw_input('Salary:')

print '''Personal information of %s:
        Name: %s
        Age:  %s
        Job:  %s
        Salary: %s
----------------------------'''%(name,name,age,job,salary)