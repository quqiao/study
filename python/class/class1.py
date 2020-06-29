#coding=utf-8
'''
Created on 2016年5月3日

@author: quqiao
'''

class Employee:
    '所有员工的基类'
    empCount=0
    
    def __init__(self,name,salary,age):
        self.name=name
        self.salary=salary
        self.age=age
        Employee.empCount+=1
        
    def displayCount(self):
        print "Total Employee %d" %Employee.empCount
        
    def displayEmployee(self):
        print "Name:",self.name,",Salary:",self.salary,",Age:",self.age
        
        
"创建Employee类的第一个对象"
emp1=Employee("Zara",2000,0)
emp1.displayEmployee() 
emp1.displayCount()
"创建Employee类的第二个对象"
emp2=Employee("Manni",5000,1)


emp2.displayEmployee()

emp2.displayCount()
#setattr(emp2, 'age', 9)




#print "Total Employee %d" % Employee.empCount
#print hasattr(emp1, 'age')
#print hasattr(emp1, 'font')
#print getattr(emp2, 'salary')

