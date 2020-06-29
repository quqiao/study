"""
网络爬虫：称为网络蜘蛛，网络机器人，网页追随者

流程：
1.获取初始URL，URL初始地址是用户自己制定的开始爬取的网页
2.爬取对应的URL地址网页时候，获取新的URL地址
3.将新的URL的地址放到URL队列中
4.从URL队列中读取新的URL,然后依据新的URL爬取网页，同时从新的网页中获取新的URL地址，重复上述过程
5.设置停止条件，如果没有设置停止条件时，爬虫会一直爬下去，知道无法获取新的URL地址为止，设置了停止
              条件后，爬虫将会满足停止条件时停止爬取

urllib模块
urllib.request 该模块定义了打开URL（主要是HTTP)的方法和类，例如，身份验证，重定向，cookie等等
urllib.error 该模块中主要包含异常类，基本的异常类是URLError
urllib.parse 该模块定义的功能分为两大类，URL解析和URL引用
urllib.robotparser  该模块用于解析robots.txt文件

scrapy爬虫框架
    一套比较成熟的Python爬虫框架，简单轻巧，并且非常方便，可以高效率地爬取Web页面并从页面中提取结构化的数据

Crawley爬虫框架
    python开发出的爬虫框架，该框架致力于改变人们从互联网中提取数据的方式

PySpider爬虫框架
    python语言编写，分布式架构，支持多种数据库后端，强大的WebUI支持脚本编辑器，任务监视器，项目管理器以及
    结果结果查看器
"""

import urllib.request
import urllib.parse

"""通过get方法获取网页"""
# # 打开指定开始爬取的网页
# response = urllib.request.urlopen("http://www.baidu.com")
# # 读取网页代码
# html = response.read()
# # 打印读取的内容
# print(html)

"""通过post方法获取网页"""
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
response = urllib.request.urlopen('http://www.baidu.com/post', data=data)
html = response.read()
print(html)


