#coding=utf-8
'''
Created on 2016年12月16日

@author: quqiao
'''

#作业要求
#编写登录接口：
#-输入用户名密码
#-认证成功后显示欢迎信息
#-输错三次后锁定
'''pw = raw_input('请输入密码：')

if pw=='123456':
    print '输入成功！'
        
else:
    count=3
    while count>1:
        count-=1
        print '输入错误请重试！'
        pw = raw_input('请输入密码：')       
    else:
        print '你没有机会了！'
'''        

import sys
retry_limit =3
retry_count =0
account_file = 'account.txt'
lock_file = 'account_lock.txt'

while retry_count<retry_limit:    #只要重试不超过3次就不断循环
    username = raw_input('Username:')
    lock_check = file(lock_file) #当用户输入用户名后，打开LOCK文件以检查是否此用户已经LOCK了
    
    for line in lock_check.readline():#循环Lock文件
        #line = line.split
        #if username == line[0]   全匹配
        if username in line:
            sys.exit('User %s is locked!')#如果LOCK了就直接退出
    password = raw_input('Password:')
    
    f = file(account_file,'rb') #打开账号文件
    match_flag =False #默认为FALSE，如果用户match上来，就设置为true
    for line in f.readlines():
        user,passwd=line.strip('\n').split()
        #去掉每行多余的\n并把这一行按空格分成两列，分别赋值为user，passwd两个变量
        if username == user and password == passwd:
            #判断用户名和密码是否都相等
            print 'Match', username
            match_flag = True
            #相等就把循环歪的match_flag变量改为了True
            break
            #然后就不用继续循环了，直接跳出，因为已经match上了
    f.close()
    if match_flag == False:
        #如果match_flag还为False,代表上面的循环中根本就没有match上用户名和密码，所以需要继续循环
        print 'User unmatched!'
        retry_count +=1
    else:
        print 'welcome login oldBoy Learning system!'
else:
    print 'Your account is locked!'
    f=file(lock_file,'ab')
    f.write(username)
    f.close()
        
    
    
            
        
    