#coding:gbk
import urllib
import urllib2
import string
import socket,re
import time
from bs4 import BeautifulSoup
import hashlib
socket.setdefaulttimeout(600)
def md5sum(obj):
     md5=hashlib.md5(obj.encode('gb2312')).hexdigest()
     return md5
def chkpwd(obj):
    if obj!='':
        s=md5sum(stu+md5sum(obj)[:30].upper() + '10298')[:30].upper()
        dsdsdsdsdxcxdfgfg=s
        return s
    else:
        dsdsdsdsdxcxdfgfg=obj
        return obj
def chkyzm(obj):
    if obj!='':
        s=md5sum(md5sum(obj.upper())[:30].upper() + '10298')[:30].upper()
        fgfggfdgtyuuyyuuckjg=s
        return s
    else:
        fgfggfdgtyuuyyuuckjg=obj
        return obj

def xszxcl(htm):
	#学生正选网页
    soup=BeautifulSoup(htm)
    skbjval=''
    sel_xq='1'
    ids=soup.find_all(onclick='openWinDialog(this,0)')[0]['value']
    url='stu_xszx_chooseskbj.aspx?lx=ZX&id='+ids+"&skbjval="+skbjval+"&xq="+sel_xq
    return url

class opener():
    def __init__(self,IndexUrl):
        import requests
        self.cookies=''
        self.ss=requests.session()
        self.home=IndexUrl
        self.lgurl=IndexUrl+'/_data/index_LOGIN.aspx'
        self.yzmurl = IndexUrl+'/sys/ValidateCode.aspx'
        self.yxurl = IndexUrl+'/wsxk/stu_xsyx.aspx'
		#临时修改，暂时用字符串拼接
    def start(self):
        p1headers={
        "Host":self.home.split("//")[1].strip("/"),
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding":"gzip, deflate",
        "Referer":self.home,
        "Connection":"keep-alive",
        "Upgrade-Insecure-Requests":"1"
        }
        ValidHeaders={
        "Host":self.home.split("//")[1].strip("/"),
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0",
        "Accept":"*/*",
        "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding":"gzip, deflate",
        "Referer":self.lgurl,
        "Connection":"keep-alive"
                }
        lgu=self.ss.get(self.lgurl,headers=p1headers)
        lgtxt=lgu.text
        sp=BeautifulSoup(lgtxt)
        viewstate=sp.find("input",attrs={"name":"__VIEWSTATE"})
        # return viewstate
        vi=viewstate.attrs['value']
        img=self.ss.get(self.yzmurl,headers=ValidHeaders).content
        #test
        self.ViewState=vi
        return img
    def SetData(self,user="",pwd='',validcode=''):
        self.user = user
        self.pwd = pwd
        self.ValidateCode = validcode
    def md5sum(self,obj):
        md5 = hashlib.md5(obj.encode('gb2312')).hexdigest()
        return md5
    def chkpwd(self,obj):
        if obj != '':
            s = md5sum(stu + md5sum(obj)[:30].upper() + '10298')[:30].upper()
			#'10298'为学校代码，自行查看，后续更新可能会加上
            dsdsdsdsdxcxdfgfg = s
            return s
        else:
            dsdsdsdsdxcxdfgfg = obj
            return obj
    def chkyzm(self,obj):
        if obj != '':
            s = md5sum(md5sum(obj.upper())[:30].upper() + '10298')[:30].upper()
            fgfggfdgtyuuyyuuckjg = s
            return s
        else:
            fgfggfdgtyuuyyuuckjg = obj
            return obj
    def login(self):
        headerss={
                    "Accept":"text/html, application/xhtml+xml, image/jxr, */*",
                    "Referer":self.lgurl,
                    "Accept-Language":"zh-CN",
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
                    "Content-Type":"application/x-www-form-urlencoded",
                    "Accept-Encoding":"gzip, deflate",
                    "Host":self.home.split("://")[1],
                    "Connection":"Keep-Alive",
                    "Pragma":"no-cache"

        }
        dictss={}
        dictss["__VIEWSTATE"]=self.ViewState
        dictss["pcInfo"]="Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0Windows NT 10.0; WOW645.0 (Windows) SN:NULL"
        dictss["typeName"]=u"学生".encode("gb2312")
        cpwd=self.chkpwd(self.pwd)
        yzms=self.chkyzm(self.ValidateCode)
        dictss['dsdsdsdsdxcxdfgfg']=cpwd
        dictss['fgfggfdgtyuuyyuuckjg']=yzms
        print yzms
        dictss['Sel_Type']="STU"
        dictss["txt_asmcdefsddsd"]=self.user
        dictss["txt_pewerwedsdfsdff"]=''
        dictss["txt_sdertfgsadscxcadsads"]=""
        dictss["sbtState"]=""
        #发送请求
        lgresult=self.ss.post(self.lgurl,data=dictss,headers=headerss)
        text=lgresult.text
        if re.search(u"帐号或密码不正确",text):
            return "PwdError"
        elif re.search(u'正在加载权限',text):
            return "Success"
		else:
			return "ReqHeaderError"
    def yuxuanget(self):
		#预选网页
        pass


a=opener()
b=a.start()