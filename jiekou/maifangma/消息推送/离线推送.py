#coding=utf-8
'''
Created on 2017年1月10日

@author: quqiao
'''

#coding=utf-8
'''
Created on 2015年11月30日

@author: admin
'''
import pycurl
import StringIO
import urllib





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
    test_url = "http://passport.maifangma.com/login"
    #test_data = {"version":"1.0.0","deviceType":2,"cityId":51010000,"encryMode":2,"deviceType":"2","cityId":"51010000","encryMode":"2","account":"admin","password":"123456","type":1}
    test_data="version=1.0.0&deviceNo=72465872a0ff482784a8985615792f4f&deviceType=2&cityId=51010000&data={\"account\":\"admin\",\"password\":\"123456\",\"type\":\"1\"}"
    test_url1 = "https://test.admin.maifangma.com/pushinform/insert"
    test_data1 = {"type":1,"userType":"0","userArea":"0","clock":True,"title":"biaoti","content":"xiaoxi"}
    print PostData2(c,test_url,test_data)
    #print PostData1(c,test_url1,test_data1)

    





