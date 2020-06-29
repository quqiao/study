#coding=utf-8
'''
Created on 2016年5月3日

@author: quqiao
'''

import re

line="Cats are smarter than dogs";

matchObj=re.match(r'dogs', line, re.M|re.I)
if matchObj:
    print "match -->matchObj.group():",matchObj.group()
else:
    print "No match!!"
    
matchObj=re.search(r'dogs', line, re.M|re.I)
if matchObj:
    print "search -->matchObj.group():",matchObj.group()
else:
    print "No match!!"