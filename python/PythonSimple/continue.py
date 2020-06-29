#coding=utf-8
'''
Created on 2015年11月11日

@author: quqiao
'''
while True:
    s = raw_input("Enter something:")
    if s == "quit":
        break
    if len(s) < 3:
        continue
    print "input is of suttfficient length"
    #Do other kinds of processing here...