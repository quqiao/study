#coding=utf-8
'''
Created on 2016年4月22日

@author: quqiao
'''

import time

try:
    f=file('poem.txt')
    while True:#our usual file-reading idiom
        line=f.readline()
        if len(line)==0:
           break
        time.sleep(2)
        print line,
        
finally:
    f.close()
    print 'Cleaning up...closed the file'