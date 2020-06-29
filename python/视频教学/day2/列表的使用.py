#coding=utf-8
'''
Created on 2017年1月3日

@author: quqiao
'''
'''
#name_list.pop() 默认删除最后一个
    

name_list = ['alex','jack','old gou']

print name_list[1]
print name_list[2]

name_list.append('Eric') #增加
print name_list

name_list.insert(2, '110')#插入
print name_list

name_list.remove('110')#删除值
print name_list

del name_list[1]# 根据下标删除，通用方法，不是列表自有方法


print name_list.count('jack')#统计出现次数

print name_list.index('alex')#索引

name_list.reverse() #倒序
print name_list

name_list.sort() #按照首字母ASCII码排序
print name_list

name_list.extend('abcdef')#扩展    
print name_list

info=[1,2,3,4,5,6]
name_list.extend(info)#列表扩展即列表的相加
print name_list

print name_list[name_list.index(2):name_list.index(2)+3]
print name_list[name_list.index(2):name_list.index(2)+4]
'''

#循环取相同的值
name_list2=[1,2,4,6,7,2,1,1,2,4,6,7]
first_pos = 0
for i in range(name_list2.count(2)): #先找出一共有多少个2，就循环多少次
    new_list = name_list2[first_pos:]#第一次循环name=name_list,接下来每次循环，new_list都是从上一次找的2的位置+1后开始的
    next_pos=new_list.index(2)+1 #确定下一次循环的开始位置
    print 'Find postion:',new_list.index(2),'Next:' ,next_pos #0+12
    first_pos += next_pos #0+13，因为每次查找都是从0真正开始，所有为了让程序下一次能跳过上一次已经找到的2，而直接找新的2，需要把之前找过的位置都加起来
    

''' 
name_list3=range(30)
print name_list3
print name_list3[::2] #隔一个取
print name_list3[1::2]
'''

name_list4=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
print name_list4[1:5] #[2,3,4,5]
print name_list4[:8] #[1,2,3,4,5,6,7,8]
print name_list4[5:] #[6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
print name_list4[-5:-1] #[18,19,20,21,22]
print name_list4[6:-1]
print name_list4[::2]
print name_list4[1::2]
print name_list4[-1:-5]#不能切片





