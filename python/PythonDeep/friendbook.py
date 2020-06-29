#coding=utf-8
'''
Created on 2016年4月25日

@author: quqiao
'''

import cPickle as p
import os
from email import email

fb={'test1':'cneds@fnedf.com',
    'test2':'fev@fe.com',
    'test3':'fexok@ver.com',
    'test4':'stif@qq.com'
    }


def Dumpfile():
    f=file(fb,'W')
    p.dump(list,f)
    f.close()
    
    
if os.path.isfile('fb.data'):
   friendab='fb.data'
else:
   os.touch('friendab.data')
   Dumpfile(fb)
   del fb
f=file(fb)
frilist=p.load(f)




class Person:
    def __init__(self,name):
        self.name=name
    def saysome(self):
        print 'The friedn %s,his E-mail is %s'%(sname,frilist[sname])
        
class addPerson:
    def __init__(self,name,email):
        self.name=name
        self.email=email
    def addbook(self):
        fb=frilist
        fb[sname]=email
        Dumpfile(fb)
        del fb
        print 'Successful!'
        
class delPerson:
    def __init__(self,name):
        self.name=name
    def delbook(self):
        fb=frilist
        fb.pop(sname)
        Dumpfile(fb)
        del fb
        print 'Success DEL'
        
class alterPerson:
    def __init__(self,name,email):
        self.name=name
        self.email=email
    def alterbook(self):
        fb=frilist
        fb[sname]=email
        Dumpfile(fb)
        del fb
        print 'Successfull update!'
        
print '''\
this program prints files to the standard output.
any number of file can be specified.
Options include:
[1]:Search your friedn's email from friendsbook
[2]:add your friend's email to friendsbook
[3]:del your friend's email from friendsbook
[4]:alter your friend's email from friendsbook
[5]:All friends list
[6]:exit the program
'''
        
num=raw_input('Press the number[1,2,3,4,5]-->')

if (num=='1'):
    sname=raw_input('Enter the name-->')
    if sname in frilist:
        p=Person(sname)
        p.saysome()
    else:
        print 'Not in it'
elif(num=='2'):
    sname=raw_input('Enter the name-->')
    email=raw_input('Enter the email-->')
    pa=addPerson(sname,email)
    pa.addbook()
    #p=Person(sname)
    #p.saysome()
    print frilist
elif(num=='3'):
    sname=raw_input('Enter the name-->')
    pa=delPerson(sname)
    pa.delbook()
elif(num=='4'):
    sname=raw_input('Enter the email-->')
    if sname in frilist:
        email=raw_input('Enter the email-->')
        p=alterPerson(sname,email)
        p.alterbook()
    else:
        print 'Not in it'
elif(num=='5'):
    print frilist
elif(num=='6'):
    print 'Bye!'
else:
    print 'Please input the right number'
        
    
        
    
    
        
        

            
            
    

