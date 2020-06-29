#coding=utf-8
'''
Created on 2016年9月9日

@author: quqiao
'''
import pycurl
import urllib
import StringIO
import encrypt
import demjson
def PostData(curl,url,data):

    head = ["Accept:*/*"
            ,"User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (sKHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11"
            ,'Accept:*/*' 
            ,'Content-Type:application/x-www-form-urlencoded',  
            ]
    buf = StringIO.StringIO()
    curl.setopt(pycurl.SSL_VERIFYPEER,False)
    curl.setopt(pycurl.HTTPHEADER,head)
    curl.setopt(pycurl.POSTFIELDS,urllib.urlencode(data))
    curl.setopt(pycurl.WRITEFUNCTION,buf.write)
    curl.setopt(pycurl.URL,url)
    curl.setopt(pycurl.CUSTOMREQUEST,"POST")
    curl.perform()
    the_page=buf.getvalue()
    buf.close()
    return the_page

if __name__=='__main__':
    token  ="72465872a0ff482784a8985615792f4f"
    c = pycurl.Curl()
    login_url = "http://test.passport.maifangma.com/login"
    login_data="version=1.0.0&deviceNo=72465872a0ff482784a8985615792f4f&deviceType=2&cityId=51010000&data={\"account\":\"18008062016\",\"password\":\"123456\",\"type\":\"2\"}"
    encrypt.initSdk(token)
    deskey=encrypt.getToken()
    signature=encrypt.signature(login_data, deskey)
    strencrypt= encrypt.encrypt("{\"account\":\"18008062016\",\"password\":\"123456\",\"type\":\"2\"}",deskey)
    login_data2={"sign":signature,
                 "version":"1.0.0",
                 "deviceNo":"72465872a0ff482784a8985615792f4f",
                 "deviceType":"2",
                 "cityId":"51010000" ,
                 "data": strencrypt}
    print "登录：",PostData(c, login_url, login_data2)
    data2=demjson.decode(PostData(c,login_url,login_data2))
    data3=data2.get('data')
    dencryptData=encrypt.dencrypt(data3,deskey)
    print dencryptData
    dict1=eval(dencryptData)
    print "ticketId:%s" %dict1.get('ticketId')
    modifymoney_data="version=1.0.0&deviceNo=72465872a0ff482784a8985615792f4f&deviceType=2&cityId=51010000"
    modifymoney_url="http://test.platforms.maifangma.com/user/modifymoney"
    signature2=encrypt.signature(modifymoney_data, deskey)
    insertorder_data2={"sign":signature2,
                       "version":"1.0.0",
                       "deviceNo":"72465872a0ff482784a8985615792f4f",
                       "deviceType":"2",
                       "cityId":"51010000",
                       "ticketId": dict1.get('ticketId')}
    print "%s" %PostData(c, modifymoney_url, insertorder_data2)
        

