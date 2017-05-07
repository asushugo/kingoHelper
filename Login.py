# encoding: utf-8


"""
@version: ??
@author: itacajsj
@license: Apache Licence 
@contact: itacajsj@outlook.com
@site: http://blog.waves-breaker.com
@software: PyCharm
@file: Login.py
@time: 2017/5/4 20:42
Login 模块
"""
import hashlib,os,re
from lxml import etree
from urllib.parse import urljoin



class Encrypt:
    def __init__(self,schoolNum,user='',pwd='',vcode=''):
        self.pwd=pwd
        self.user=user
        self.vcode=vcode
        self.school=schoolNum
        pass

    @staticmethod
    def md5(obj):
        md5 = hashlib.md5(obj.encode('gb2312')).hexdigest()
        return md5

    def EnPwd(self,pwd='',user=''):
        '''

        :param pwd: unicode str
        :param user: unicode str
        :return:dsdsdsdsdxcxdfgfg encoded str
        '''
        pwd=pwd or self.pwd
        if not pwd:
            raise Exception('No Pwd Found')
        user=user or self.user
        if not pwd:
            raise Exception('No User Found')
        dsdsdsdsdxcxdfgfg = self.md5(user + self.md5(pwd)[:30].upper() + self.school)[:30].upper()
        return dsdsdsdsdxcxdfgfg

    def Enverfy(self,vcode=''):
        vcode=vcode or self.vcode
        if not vcode:
            raise Exception('No VerfyImageCode Found')
        fgfggfdgtyuuyyuuckjg = self.md5(self.md5(vcode.upper())[:30].upper() + self.school)[:30].upper()
        return fgfggfdgtyuuyyuuckjg

class Login:
    def __init__(self,school,req):
        if isinstance(school,dict):
            self._school=school
        else:
            raise Exception('School is Not a Valid Type')
        self.req = req
        self.Enc = Encrypt(schoolNum=self._school['num'])
        self._viewstate=self.GetViewstate()

    def SetHeader(self,arg):
        '''
        add headers to request
        :return:
        '''
        header_choice = {arg:{}}
        base_header={
            "Accept": "*/*",
            "Accept-Language": "zh-CN",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "Keep-Alive",
            "Pragma": "no-cache"
        }

        try:
            index,host=self._school['index'],self._school['host']
        except Exception as e:
            raise Exception('School Info Error , Please Check Your Configration')

        header_choice['login_post']={
                                    "Referer": urljoin(self._school['index'], '/_data/index_LOGIN.aspx'),
                                    "Host": self._school['host']
                                }

        header_choice['valid']={
            "Host":self._school['host'],
            "Referer": urljoin(self._school['index'] , '/_data/index_LOGIN.aspx')
        }

        header_choice['first_login']={
            "Host": self._school['host'],
            "Referer": self._school['index']
        }
        rheader=base_header.copy()
        r1=dict(base_header,**header_choice[arg])
        return r1


    def GetViewstate(self):
        url=urljoin(self._school['index'] , '/_data/index_LOGIN.aspx')
        headers=self.SetHeader('first_login')
        response=self.req.get(url)
        tree=etree.HTML(response.text)
        viewstate = tree.xpath(r"//input[@name='__VIEWSTATE']")[0].get('value')
        self._viewstate=viewstate
        return viewstate

    def GetValidImg(self,path=os.getcwd(),raw=False):
        url=urljoin(self._school['index'], '/sys/ValidateCode.aspx')
        img = self.req.get(url, headers=self.SetHeader('valid')).content
        if os.path.isdir(path):
            f=open(os.path.join(path,'validimg.jpg'),'wb')
            f.write(img)
            f.close()
        if raw:
            return img
        else:
            return None

    def SetPostData(self,user,pwd,vcode):
        '''
        make PostData
        :return: post dict
        '''
        if not self._viewstate:
            self.GetViewstate()
        postdata = {}
        postdata["__VIEWSTATE"] = self._viewstate
        postdata[
            "pcInfo"] = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0Windows NT 10.0; WOW645.0 (Windows) SN:NULL"
        postdata["typeName"] = u"学生".encode("gb2312")
        cpwd = self.Enc.EnPwd(pwd=pwd,user=user)
        yzms = self.Enc.Enverfy(vcode=vcode)
        postdata['dsdsdsdsdxcxdfgfg'] = cpwd
        postdata['fgfggfdgtyuuyyuuckjg'] = yzms
        postdata['Sel_Type'] = "STU"
        postdata["txt_asmcdefsddsd"] = user
        postdata["txt_pewerwedsdfsdff"] = ''
        postdata["txt_sdertfgsadscxcadsads"] = ""
        postdata["sbtState"] = ""
        return postdata

    def Login(self,user,pwd,vcode):
        data=self.SetPostData(user,pwd,vcode)
        response=self.req.post(urljoin(self._school['index'], '/_data/index_LOGIN.aspx'), data=data, headers=self.SetHeader('login_post'))
        txt=response.text
        if re.search(u"登录失败", txt):
            return False,"请检查用户名,密码及验证码是否错误"
        elif re.search(u'正在加载权限', txt):
            return True,response
        else:
            return False,response



if __name__ == '__main__':
    import requests,os
    req = requests.session()
    school = {'num': '10298', 'index': 'http://jwk.njfu.edu.cn', 'host': 'jwk.njfu.edu.cn'}
    a = Login(school, req)
    a.GetValidImg()
    #a.Login()
