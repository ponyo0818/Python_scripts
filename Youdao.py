# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 15:55:13 2019
credit to Lin, modified by yfang
"""


import urllib.request
import urllib.parse
import json
import time
while True:
   content = input('Please type the content to be translated(type "e" to exit)：')
   if  content =='e':
        break
   url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'     #  有道词典的请求网址
 
   head = { }       #设置一个头部使得浏览器认为不是用python进行访问
   head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
 
   data ={ }
 
   data ['i'] =  content
   data ['from']  = 	'AUTO'
   data['to'] =	'AUTO'
   data['smartresult']	 = 'dict'
   data['client'] = 	'fanyideskweb'
   data['salt']=	'15565283671426'
   data['sign']=	'135c616fb0ba768c86718a8ae94e31a8'
   data['ts']=	'1556528367142'
   data['bv']=	'e2a78ed30c66e16a857c5b6486a1d326'
   data['doctype'] = 	'json'
   data['version'] = 	'2.1'
   data['keyfrom'] = 	'fanyi.web'
   data['action'] = 	'FY_BY_REALTlME'
 
 
   data = urllib.parse.urlencode(data).encode('utf-8')     #对数据进行utf-8的编码模式
 
   req = urllib.request.Request(url,data,head)    #  填充头部使得浏览器认为不是用python进行运行
 
   response = urllib.request.urlopen(req)       # 实现对网站进行访问
 
   html  = response.read().decode('utf-8')     # 对数据进行解码
 
    
   target = json.loads(html)           #  已编码的JSON字符串解码为python对象
   target = target['translateResult'][0][0]['tgt']    #对输出的target进行格式化的筛选
   print(target)
   time.sleep(5)
