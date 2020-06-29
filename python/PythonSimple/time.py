#coding=utf-8
'''
Created on 2016年5月23日

@author: quqiao
'''
import time

#time altzone()方法
print "time.altzone %d" %time.altzone


#time asctime()方法
t=time.asctime()
print "time.asctime(t):%s" %time.asctime()


#time clock()方法
def procedure():
    time.sleep(2.5)
#measure process time
t0=time.clock()
procedure()
print time.clock()-t0,"seconds process time"
#measure wall time
t0=time.time()
procedure()
print time.time()-t0,"seconds wall time"


#time ctime()方法
print "time.ctime():%s"%time.ctime()


#time gmtime()方法
print "time.gmtime():%s"%time.gmtime()


#time localtime()方法
print "time.localtim(): %s"% time.localtime()


#Python time mktime()方法
t=(2009, 2, 17, 17, 3, 38, 1, 48, 0)
secs=time.mktime(t)
print "time.mktime(t):%f"% secs
print "asctime(localtime(secs)):%s"%time.asctime(time.localtime(secs))


#time sleep()方法
print"start : %s" %time.ctime()
time.sleep(5)
print"end : %s" %time.ctime()


#time strftime()方法
t=(2009, 2, 17, 17, 3, 38, 1, 48, 0)
t=time.mktime(t)
print time.strftime("%b %d %Y %H:%M:%S",time.gmtime(t))


#time strptime()方法
struct_time=time.strptime("30 Nov 00", "%d %b %y")
print "return tuple:%s"%struct_time


#time time()方法
print "time.time():%f"%time.time()
print time.localtime(time.time())
print time.asctime(time.localtime(time.time()))



