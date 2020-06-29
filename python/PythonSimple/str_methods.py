#coding=utf-8
'''
Created on 2015年11月12日

@author: admin
'''
name = 'Swaroop' #This is a string object

if name.startswith("Swa"):
    print 'Yes,the string starts with "Swa"'

if 'a' in name:
    print 'Yes,it contains the string "a"'
    
if name.find('war')!=-1:
    print 'Yes,it contains the string "war"'
    
delimiter = '_*_'
mylist = ['Brazil','Russia','India','China']
print delimiter.join(mylist)
