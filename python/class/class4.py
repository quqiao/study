#coding=utf-8
'''
Created on 2016年6月29日

@author: quqiao
'''


class Employee:
    
    '所有员工的基类'
    empCount=0
    
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
        Employee.empCount +=1
        
    def displayCount(self):
        print "Total Employee %d" %Employee.empCount
        
    def displayEmployee(self):
        print "Name:",self.name, ",Salary:",self.salary
        
        
"创建employee类的第一个对象"
emp1=Employee("Zara",2000)
emp1.age=7
"创建employee类的第二个对象"
#emp2=Employee("Manni",5000)
emp1.displayEmployee()
#emp2.displayEmployee()

print hasattr(emp1, 'age')
print getattr(emp1,'name')
setattr(emp1, 'age', 20)
print getattr(emp1,'age')

print "Total Employee %d" %Employee.empCount
        
