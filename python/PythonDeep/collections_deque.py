#coding=utf-8
'''
Created on 2016年9月13日

@author: quqiao
'''


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
            
            
a = [1, 5, 2, 1, 9, 1, 5, 10]
c=list(dedupe(a))
print c