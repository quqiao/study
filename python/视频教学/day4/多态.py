#coding=utf-8
'''
class A:    
    def prt(self):    
        print "A"    
    
class B(A):    
    def prt(self):    
        print "B"    
            
class C(A):    
    def prt(self):    
        print "C"    
           
class D(A):    
    pass    
    
class E:    
    def prt(self):    
        print "E"    
    
class F:    
    pass    
    
def test(arg):    
    arg.prt()  
    
a = A()    
b = B()    
c = C()    
d = D()    
e = E()    
f = F()    
    
test(a)    
test(b)    
test(c)    
test(d)    
test(e)    
test(f)
'''

class Person(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
    def whoAmI(self):
        return 'I am a Person, my name is %s'%self.name
    
class Student(Person):
    def __init__(self,name,gender,score):
        super(Student,self).__init__(name,gender)
        self.score = score
    def whoAmI(self):
        return 'I am a Student, my name is %s'%self.name
    
class Teacher(Person):
    def __init__(self,name,gender,course):
        super(Teacher,self).__init__(name,gender)
        self.course = course
    def whoAmI(self):
        return 'I am a Teacher,my name is %s'%self.name

p=Person('JACK','male')
s=Student('Bob','male','99')
t=Teacher('lucy','famale','yuwen')

def who_am_i(x):
    print x.whoAmI()
    
who_am_i(p)
who_am_i(s)
who_am_i(t)