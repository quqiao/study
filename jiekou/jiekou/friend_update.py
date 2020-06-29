#coding=utf-8
'''
Created on 2015年11月30日

@author: admin
'''
import pycurl
import StringIO
import urllib
import unittest
import demjson


#class TestUrlHttpcode(unittest.TestCase):
    #def setUp(self):
        #urlinfo=['https://api.leancloud.cn/1.1/functions/friends_update/']
        #self.checkurl=urlinfo
    
    #def test_OK(self):
        #test=demjson.decode(PostData1(c,test_url1,test_data1))
        #self.assertEqual(test.get(''),'quqiao1@gmail.com')
            


def PostData1(curl, url, data):
    head = ["Accept:*/*"
            ,"User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11"
            ,"Content-Type:application/x-www-form-urlencoded"
            ,"X-AVOSCloud-Application-Id: dcf3uj1qrprt61ltqyhk43v5cs5m7e6xkups9i6ep6nrzg6e"
            ,"X-AVOSCloud-Application-Key: kbvvp733zwghxq3utbd9r5aq48agmpocl58xkvhk2e645f6y"
            ]

    buf = StringIO.StringIO()
    
    curl.setopt(pycurl.SSL_VERIFYPEER, False)
    curl.setopt(pycurl.HTTPHEADER,  head)
    curl.setopt(pycurl.POSTFIELDS,  urllib.urlencode(data))
    curl.setopt(pycurl.URL, url)
    curl.setopt(pycurl.WRITEFUNCTION, buf.write)
    #curl.setopt(pycurl.CUSTOMREQUEST,"POST")
    curl.perform()
    the_page = buf.getvalue() 
    #print the_page
    buf.close()
    return the_page

def PostData2(curl, url, data):
    head = ["Accept:*/*"
            ,"User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11"
            ,"Content-Type:application/x-www-form-urlencoded"
            ,"X-LC-Session:d4t6bbjuh1s9chcfqc9jzm9wp"
            ,"X-AVOSCloud-Application-Id: dcf3uj1qrprt61ltqyhk43v5cs5m7e6xkups9i6ep6nrzg6e"
            ,"X-AVOSCloud-Application-Key: kbvvp733zwghxq3utbd9r5aq48agmpocl58xkvhk2e645f6y"
            ]

    buf = StringIO.StringIO()
    
    curl.setopt(pycurl.SSL_VERIFYPEER, False)
    curl.setopt(pycurl.HTTPHEADER,  head)
    curl.setopt(pycurl.POSTFIELDS,  urllib.urlencode(data))
    curl.setopt(pycurl.URL, url)
    curl.setopt(pycurl.WRITEFUNCTION, buf.write)
    curl.setopt(pycurl.CUSTOMREQUEST,"PUT")
    curl.perform()
    the_page = buf.getvalue()
    #print the_page
    buf.close()
    return the_page

if __name__=='__main__':
    c = pycurl.Curl()
    test_url = "https://api.leancloud.cn/1.1/functions/friends_update"
    test_url1 = "https://leancloud.cn/1.1/login"
    test_data1 = {"username":"quqiao@gmail.com","password":"123456"}
    test_data2={"friend":"567a67b360b25aa3dcb335d0"}
    #unittest.main()


    print PostData1(c,test_url1,test_data1)
    #print PostData2(c,test_url,test_data2)
    pass
    





