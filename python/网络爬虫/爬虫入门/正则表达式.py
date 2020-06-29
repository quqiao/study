#coding=utf-8


import re
'''
# 将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串”
pattern = re.compile(r'hello')

# 使用re.match匹配文本，获得匹配结果，无法匹配时将返回None
result1 = re.match(pattern, 'hello')
result2 = re.match(pattern, 'helloo CQC!')
result3 = re.match(pattern, 'helo CQC!')
result4 = re.match(pattern, 'hello CQC!')

if result1:
    print result1.group()
else:
    print '1匹配失败！'
    
if result2:
    print result2.group()
else:
    print '2匹配失败！'  
    
if result3:
    print result3.group()
else:
    print '3匹配失败！'
    
if result4:
    print result4.group()
else:
    print '4匹配失败！'
'''

m = re.match(r'(\w+) (\w+)(?P.*)','hello world!')

print "m.string:",m.string
print "m.re:",m.re
print "m.pos:",m.pos
print "m.endpos:",m.endpos
print "m.lastindex:",m.lastindex
print "m.lastgroup:",m.lastgroup
print "m.group():",m.group()
print "m.group(1,2)",m.group(1,2)
print "m.groups()",m.groups()
print "m.groupdict()",m.groupdict()
print "m.start(2)",m.start(2)
print "m.end(2):",m.end(2)
print "m.span(2):",m.span(2)
print r"m.expand(r'\g \g\g'):",m.expand(r'\2 \1\3')