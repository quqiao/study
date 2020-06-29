# -*- coding: utf-8 -*-
__author__ = 'quqiao'

"""
爬虫的基本原理：
1. 模拟http请求，请求发送到目标网址
    urllib.request  openurl(url)
    Request 定制header 反爬虫
2. 获得html
    read()
3. 数据解析---从海量数据中提取我们需要的部分
    正则
    字符串
    BeautifulSoup
4. 数据存储---存储到文件，打印输出，数据库
    文件存储:with open () as f:
    存到数据库:MySQL:pymysql, mysql-connector
"""

import urllib.request
from bs4 import BeautifulSoup
import pymysql

movielist = []
url = "https://movie.douban.com/chart"

def get_html(url):
    """模拟http请求并获取html"""
    res = urllib.request.urlopen(url)
    html = res.read().decode()
    return html

def parse_html(htmlfile):
    """
    解析html
    :param htmlfile:
    :return:
    """
    mysoup = BeautifulSoup(htmlfile, 'html.parser')
    movie_zone = mysoup.find("ol")
    movie_list = movie_zone._find_all("li")
    for movie in movie_list:
        movie_name = movie.find("span", attrs={'class': 'title'}).getText()
        movielist.append(movie_name)
        nextpage = mysoup.find('span', attrs={'class': 'title'}).find('a')
    if nextpage:
        new_url = url + nextpage['href']
        parse_html(get_html(new_url))

def save_data(movielist):
    conn = pymysql.connect(host="localhost", user="root", password="mysql", db="test")
    mycursor = conn.cursor()
    sql = 'CREATE TABLE movie250(ID VARCHAR(10), name VARCHAR(20)) DEFAULT CHARSET=utf8'
    mycursor.execute(sql)
    sql = ''
    for id, movie in enumerate(movielist):
        sql = "INSERT INTO movie250 VALUE(%s, %s)"
        mycursor.execute(sql, (id,movie))
    mycursor.close()
    conn.close()

reshtml = get_html(url)
parse_html(reshtml)
print(movielist)


