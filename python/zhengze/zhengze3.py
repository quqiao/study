#coding=utf-8
'''
Created on 2016年5月3日

@author: quqiao
'''

import re


phone="2004-959-599 #this is phone number"

#Delete Python-style Comments
num=re.sub(r'#.*$',"",phone)
print "Phone Num:",num

#Remove anything other than digits
num=re.sub(r'\D',"",phone)
print "Phone Num:",num
