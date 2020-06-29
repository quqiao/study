#coding=utf-8
'''
Created on 2016年4月27日

@author: quqiao
'''

import thread   
#from time import sleep,ctime
import time

def loop0():
    print '+++start loop 0 at:',time.ctime()
    time.sleep(4)
    print '+++loop 0 done at:',time.ctime()
    
def loop1():
    print '***start loop 1 at:',time.ctime()
    time.sleep(2)
    print '***loop 1 done at:',time.ctime()
    
def main():
    print '------starting at:',time.ctime()
    thread.start_new_thread(loop0, ())
    thread.start_new_thread(loop1, ())
    time.sleep(6)
    print '------all DONE at:',time.ctime()
    
if __name__=='__main__':
    main()
