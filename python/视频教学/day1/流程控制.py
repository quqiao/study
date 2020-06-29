#coding=utf-8
'''
Created on 2016年12月15日

@author: quqiao
'''

#for 循环
#if语句
name = raw_input("Please input your name:")
#age  = input('age:')
job  = raw_input('Job:')
salary = raw_input('Salary:')

raal_age=29

for i in range(10):
    #real_age = 29
    age  = input('age:')
    if age>29:
        print 'think smaller!'
    
    elif age<29:
        print 'think bigger!'
    
    elif age==29:
        print 'you are right!'
        break
    #else:
        #msg = 'you are still quite young'
    if 9-i != 0:
        
        print 'you still got %s shots!' %(9-i)
    if 9-i == 0:
        print '机会有用完'

    

print '''Personal information of %s:
        Name: %s
        Age:  %s
        Job:  %s
        Salary: %s
----------------------------
%s
'''%(name,name,age,job,salary)


