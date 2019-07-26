# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 16:06:24 2019
This APP is used to return the translate result using 2 online dictionary: 
    youdao and 21 century

credit to chongshangyunxiao on CSDN
revised by yfang to adapt python 3.6

------------
re-Regular expression operations
https://docs.python.org/2/library/re.html

"""
import re
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import urllib.parse 

class Spider_Youdao:
    # 初始化
    def _init_(self):
        #有道网页翻译段
        self.Trans_Youdao_Tag = re.compile(r'\s.*?<li>\s?')
        #21世纪大词典段
        self.Trans_Shiji_Tag = re.compile(r'\s?<span.*?class="def".*?</span>')
        #退出标志
        self.run = True

    #获得查询的单词
    def SearchWord(self):
        S_Word = input("\n#[输入单词]\n>")

        return S_Word

    #得到URL
    def GetUrl(self):
        SWord = self.SearchWord()
        #加上查询单词以后
        if urllib.parse.quote(SWord) == SWord:
            MyUrl = "http://dict.youdao.com/search?len=eng&q="+urllib.parse.quote(SWord)+"&keyfrom=dict.top"
            return MyUrl

    #获取页面
    def GetPage(self):
        #获取URL
        Youdao_Url = self.GetUrl()
        #伪装成浏览器请求
        user_agent = 'Mozilla/5.0(X11;Ubuntu;Linux x86_64;rv:32.0)Gecko/20100101 Firefox/32.0'
        headers = {'User-Agent':user_agent}
        req = urllib2.Request(Youdao_Url,headers = headers)
        Res = urllib2.urlopen(req)
        #将其他编码的字符串转换成Unicode编码
        ResultPage =  Res.read().decode("utf-8")
        return ResultPage


    #开始提取网页中的信息
    def ExtractPage(self):
        #获取页面
        MyPage = self.GetPage()
        #提取有道的基本翻译
        # YoudaoTrans = self.Trans_Youdao_Tag
        YoudaoTrans = re.compile(r'\s?<li>.*?</li>\s?')
        
        #提取21世纪词典的翻译
        # ShijiTrans = self.Trans_Shiji_Tag
        ShijiTrans = re.compile(r'\s?<span.*?class="def">.*?</span>')
        print ("----------------------------------------")
        # YouDaoTrans = self.Trans_Youdao_Tag
        YouDaoTrans = re.compile(r'\s?<li>.*?</li>\s?')
        TransYdIterator = YoudaoTrans.finditer(MyPage)
        print ("#（翻译来自有道词典）：")
        myItems = re.findall('<div.*?class="trans-container">(.*?)<div id="webTrans" class="trans-wrapper trans-tab">',MyPage,re.S)
        for item in myItems:
            YDTmp = item
        TransYdIterator = YouDaoTrans.finditer(YDTmp)
        for iterator in TransYdIterator:
            YouDao = iterator.group()
            YDTag = re.compile('\s?<.*?>')
            print (YDTag.sub('',YouDao))
        print ("--------------------------------------------")
        TransSjIterator = ShijiTrans.finditer(MyPage)
        print ("#(翻译来自21世纪大词典):")
        for iterator in TransSjIterator:
            ShiJi = iterator.group()
            SJTag = re.compile('\s?<.*?>')
            print( SJTag.sub('',ShiJi))
        print ("--------------------------------------------")


    #启动爬虫
    def Start(self):
        while True:
            S_Word = input("\n#[\"!\"号退出.回车继续.]\n>")
            if S_Word != "!":
                self.ExtractPage()
                #thread.start_new_thread(self.ExtractPage,())
                #time.sleep(5)
            else:
                # self.run = False
                break

if __name__ == '__main__':
    mydict = Spider_Youdao()
    mydict.Start()
