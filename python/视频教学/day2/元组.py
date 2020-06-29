#coding=utf-8
'''
Created on 2017年1月4日

@author: quqiao
'''

#a=(1,2,3,4,5)
#print type(a)
#print list(a)
#print type(list(a))

import sys,os
if len(sys.argv)<=4:
    print "usage:./file_replace.py  old_text  new_text filename"
old_text,new_text = sys.argv[1],sys.argv[2]
file_name = sys.argv[3]

f= file(file_name,'rb')
new_file = file('.%s.bak'% file_name,'wb')
for line in f.xreadlines():
    new_file.write(line.replace(old_text,new_text))
f.close()
new_file.close()
    
if '--bak' in sys.argv:
    os.rename(file_name,'.%s.bak2'%file_name)
    os.rename('.%s.bak'%file_name,file_name) 
else:
    os.rename('.%s.bak'%file_name,file_name)
    