# coding=utf-8
#----------------------------------------
#2016.9.9 增加无需求文档时的适配
#----------------------------------------
import Excel
import codecs
import re
import os


excel=Excel.Excel()
reqexcel=Excel.Excel()
#测试用例excel名称
featurename=u"D:/资料/测试用例/test2/IDEALENS VR Web1.1-安全测试.xlsx"
#需求模板Excel名称
requirename=u"D:/资料/测试用例/test2/IDEALENS VR Web1.1-安全测试需求-30.xls"
#requirenamelist=featurename.split("/")
#requirenamelist[len(requirenamelist)-1]=requirenamelist[len(requirenamelist)-1].replace(u"测试用例",u"需求模板")
#requirename="/".join(requirenamelist)
#if os.path.exists(requirename):
#    pass
#else:
#    requirename=requirename[:-1]

reqList={}
reqstring=u"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
reqstring+=u"<requirements>\n"
if os.path.exists(requirename):
    reqexcel.open_excel(requirename)
    requireNumber=reqexcel.worksheet.nrows
    statusList={"4.0":"F","":"R"}
    for i in range(1,requireNumber):
        reqid=reqexcel.get_value(i,0)
        reqtitle=reqexcel.get_value(i,1)
        reqdes=reqexcel.get_value(i,2).replace("\n","<br />")
        reqstatus=reqexcel.get_value(i,3)
        reqtype=reqexcel.get_value(i,4)
        reqnumber=reqexcel.get_value(i,5)
        reid= reqid
        print reid
        reqList[reid]={}
        reqList[reid]["id"]=reqid
        reqList[reid]["title"]=reqtitle
        reqList[reid]["des"]=reqdes
        reqList[reid]["status"]=reqstatus
        reqList[reid]["type"]=reqtype
        reqList[reid]["number"]=reqnumber
        reqstring+=u"\t<requirement>\n"
        reqstring+=u"\t\t<docid><![CDATA[%s]]></docid>\n"%reqid
        reqstring+=u"\t\t<title><![CDATA[%s]]></title>\n"%reqtitle
        reqstring+=u"\t\t<node_order><![CDATA[%s]]></node_order>\n"%(i-1)
        reqstring+=u"\t\t<description><![CDATA[%s]]></description>\n"%reqdes
        if (statusList.has_key(str(reqstatus))):
            reqstring+=u"\t\t<status><![CDATA[%s]]></status>\n"%statusList[str(reqstatus)]
        else:
            reqstring+=u"\t\t<status><![CDATA[R]]></status>\n"
            
        if (reqtype==""):
            reqstring+=u"\t\t<type><![CDATA[3]]></type>\n"
        else:
            reqstring+=u"\t\t<type><![CDATA[%d]]></type>\n"%reqtype
        reqstring+=u"\t\t<expected_coverage><![CDATA[%d]]></expected_coverage>\n"%reqnumber
        reqstring+=u"\t</requirement>\n"

reqstring+=u"</requirements>"

excel.open_excel(featurename)
suitename=excel.worksheet.name
rowNumber=excel.worksheet.nrows
caseList={}
lastcasename=""
casenamelist=[]        
xmlstring=u"<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n"
xmlstring+=u""
for i in range(1,rowNumber):
    casename=excel.get_value(i,0)
    caselevel=excel.get_value(i,1)
    caseopttype=excel.get_value(i,2)
    casekeyword=excel.get_value(i,3)
    caseremark=excel.get_value(i,4)
    caseprepare=excel.get_value(i,5)
    caseopt=excel.get_value(i,6).replace("\n","<br />\n")
    caseexp=excel.get_value(i,7).replace("\n","<br />\n")
    caseexectype=excel.get_value(i,8)
    casereq=excel.get_value(i,9)
    if casename=="":
        caseList[lastcasename]["caseoptlist"].append(caseopt)
        caseList[lastcasename]["caseexplist"].append(caseexp)
        caseList[lastcasename]["execlist"].append(caseexectype)
    else:
        print "casename%s"%casename
        casenamelist.append(casename)
        caseList[casename]={}
        caseList[casename]["casename"]=casename
        print "importance:%s"%caselevel
        caseList[casename]["importance"]=caselevel
        caseList[casename]["opttype"]=caseopttype
        caseList[casename]["keyword"]=casekeyword
        caseList[casename]["remark"]=caseremark
        caseList[casename]["prepare"]=caseprepare
        caseList[casename]["execlist"]=[caseexectype]
        caseList[casename]["req"]=casereq
        caseList[casename]["caseoptlist"]=[caseopt]
        caseList[casename]["caseexplist"]=[caseexp]
        lastcasename=casename
        
    
xmlstring+=u"<testsuite name=\"%s\" >\n"%featurename.split("/")[-1].replace(".xlsx","").replace(".xls","")
xmlstring+=u"<testsuite name=\"%s\" >\n"%suitename

for k in reqList.keys():
    print k

j=1
importance={"High":3,"Medium":2,"Low":1,"1.0":1,"2.0":2,"3.0":3,"1":1,"2":2,"3":3}
print importance["3.0"]
for k in casenamelist:
    print caseList[k]["prepare"]
    xmlstring+=u"<testcase name=\"%s\">\n"%caseList[k]["casename"]
    xmlstring+=u"<node_order><![CDATA[%s]]></node_order>\n"%j
    xmlstring+=u"<summary><![CDATA[%s]]></summary>\n"%caseList[k]["remark"]
    xmlstring+=u"<preconditions><![CDATA[%s]]></preconditions>\n"%caseList[k]["prepare"]
    xmlstring+=u"<execution_type><![CDATA[%s]]></execution_type>\n"%caseList[k]["opttype"]
    xmlstring+=u"<importance><![CDATA[%s]]></importance>\n"%importance[str(caseList[k]["importance"])]
    xmlstring+=u"<steps>\n"
    j=j+1
    for i in range(0,len(caseList[k]["caseoptlist"])):
        xmlstring+=u"<step>\n"
        xmlstring+=u"<step_number><![CDATA[%s]]></step_number>\n"%(i+1)
        xmlstring+=u"<actions><![CDATA[%s]]></actions>\n"%caseList[k]["caseoptlist"][i]
        xmlstring+=u"<expectedresults><![CDATA[%s]]></expectedresults>\n"%caseList[k]["caseexplist"][i]
        print caseList[k]["execlist"][i]
        xmlstring+=u"<execution_type><![CDATA[%s]]></execution_type>\n"%caseList[k]["execlist"][i]
        xmlstring+=u"</step>\n"
        
    xmlstring+=u"</steps>\n"
    xmlstring+=u"<keywords><keyword name=\"%s\"></keyword>\n"%caseList[k]["keyword"]
    xmlstring+=u"</keywords>\n"
    
    print caseList[k]["remark"]
    if os.path.exists(requirename):
        xmlstring+=u"<requirements>\n"
        xmlstring+=u"<requirement><doc_id><![CDATA[%s]]></doc_id></requirement>\n"%reqList[caseList[k]["req"]]["id"]
        xmlstring+=u"</requirements>\n"
    else:
        xmlstring+=u"<requirement><doc_id><![CDATA[]]></doc_id></requirement>\n"
    
    xmlstring+=u"</testcase>\n"
    
xmlstring+=u"</testsuite>\n"
xmlstring+=u"</testsuite>\n"

if os.path.exists(requirename):
    file_object = codecs.open(requirename.replace("xlsx","xml").replace("xls","xml"),'w',"utf-8")
    try:
        file_object.write(reqstring)
    finally:
        file_object.close()
    
file_object = codecs.open(featurename.replace("xlsx","xml").replace("xls","xml"),'w',"utf-8")
try:
    file_object.write(xmlstring)
finally:
    file_object.close()