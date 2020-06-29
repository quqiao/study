#coding=utf-8
'''
Created on 2016年5月24日

@author: quqiao
'''

def printdefault(name,age=30):
    
    print "Name:",name;
    print "Age:",age;
    return;

printdefault(age=50, name="test001")
printdefault( name="test002")
printdefault( age=60,name="test003")


