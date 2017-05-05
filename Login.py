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
import hashlib

class Encrypt:
    def __init__(self,schoolNum,user='',pwd='',verifyimg=''):
        self.pwd=pwd
        self.user=user
        self.vimg=verifyimg
        self.school=schoolNum
        pass

    @staticmethod
    def md5(obj):
        md5 = hashlib.md5(obj.encode('gb2312')).hexdigest()
        return md5

    def EnPwd(self,pwd='',user=''):
        '''

        :param pwd: unicode str
        :param user: uunicode str
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

    def Enverfy(self,vimg=''):
        vimg=vimg or self.vimg
        if not vimg:
            raise Exception('No VerfyImageCode Found')
        fgfggfdgtyuuyyuuckjg = self.md5(self.md5(vimg.upper())[:30].upper() + self.school)[:30].upper()
        return fgfggfdgtyuuyyuuckjg

class Login:
    def __init__(self,school,req):
        if isinstance(dict,school):
            self._school=school
        else:
            raise Exception('School is Not a Valid Type')
        self.req = req
        self.Enc = Encrypt(schoolNum=self._school['num'])
        self.viewstate=''
    def SetHeader(self):
        '''
        add headers to request
        :return:
        '''
        from urllib.parse import urljoin

        try:
            index,host=self._school['index'],self._school['host']
        except Exception as e:
            raise Exception('School Info Error , Please Check Your Configration')
        refer=urljoin(self._school['index'], '/_data/index_LOGIN.aspx')

        headers = {
            "Accept": "text/html, application/xhtml+xml, image/jxr, */*",
            "Referer": refer,
            "Accept-Language": "zh-CN",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "gzip, deflate",
            "Host": self._school['host'],
            "Connection": "Keep-Alive",
            "Pragma": "no-cache"
        }
        self.req.headers=headers

    def GetViewstate(self):
        pass

    def SetPostData(self):
        '''
        make PostData
        :return: post dict
        '''
        if not self.viewstate:
            self.GetViewstate()
