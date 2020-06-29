#coding=utf-8
'''
Created on 2016年4月21日

@author: quqiao
'''

import sys

try:
    s=raw_input('Enter something -->')
except EOFError:
    print '\n Why did you do an EOF on me?'
    sys.exit()
except:
    print '\n Some error/excepion occured.'
    #here,we are not exiting the program
    
print 'Done'
    
