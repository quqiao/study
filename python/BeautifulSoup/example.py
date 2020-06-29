#coding=utf-8
'''
Created on 2016年6月24日

@author: quqiao
'''


from bs4 import BeautifulSoup

html_doc = """
email:quqiao@gmail.com,"sessionToken":"d4t6bbjuh1s9chcfqc9jzm9wp","updatedAt":"2015-12-22T06:40:15.379Z","phone":"18612340000","objectId":"5678f04f60b25b796b4600b8","nickname":"quqiao","username":"quqiao","createdAt":"2015-12-22T06:40:15.290Z","sioeyeInfo":{"__type":"Pointer","className":"UserInfo","objectId":"5678f04fddb2160ca87e53c5"},"emailVerified":false,"searchDisable":false,"authData":null,"mobilePhoneVerified":false

"""

soup = BeautifulSoup(html_doc)

#print soup.title

#print soup.title.name

#print soup.title.string

#print soup.p

#print soup.a

print soup.find_all('email')

#print soup.find(id='link3')

#print soup.get_text()