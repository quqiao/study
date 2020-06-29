#coding=utf-8
'''
Created on 2016年12月16日

@author: quqiao
'''

#while 语句 。死循环
print_num = input('which loop do you want it to be printed out?')
count = 0
while count < 100000000:
    #print_num = input('which loop do you want it to be printed out?')
    if count == print_num:
        print 'There you got the number:',count
        choice = raw_input('Do you want to continue thr loop?(y/n)')
        if choice =='n':
            break
        else:
            while print_num<=count:
                print_num = input('which loop do you want it to be printed out?')
                print "已经过了，sx"
    else:
        print 'Loop:',count
    count +=1


else:
    print 'loop:',count