#coding=utf-8

class test():
    def __init__(self):
        print '初始化'
        
    def __del__(self):
        print '删除'
        
    def my(self):
        print '自己的方法'
        
t=test()
t.my()
del t