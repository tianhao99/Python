# -*- coding: utf-8 -*-
"""
Created on Fri May 21 15:57:53 2021

@author: kingb
"""
###电影天堂部分电影下载链接

#1、获取首页源码
#2、筛选目标代码
#3、进入下载页面获取url
#4、遍历写入文件

import requests
import re
import csv

#1、获取首页源码
url = 'https://www.dytt8.net/index.htm'
resp = requests.get(url,verify=False)
resp.encoding = 'gbk'


#2、筛选目标代码
ojb1 = re.compile('新片精品.*?<ul>(?P<sel>.*?)</ul>',re.S)
ojb2 = re.compile("]<a href='(?P<indx>.*?)'>",re.S)
ojb3 = re.compile('◎片　　名(?P<name>.*?)<br />.*?href="(?P<htt>.*?)"',re.S)
result1 = ojb1.search(resp.text)
result2 = ojb2.finditer(result1.group())

f = open('http.csv',mode='w',encoding='utf-8')
writ = csv.writer(f)
#3、进入下载页面获取url
dic = {}
for it in result2:
    resp2 = requests.get('https://www.dytt8.net'+it.group('indx'),verify=False)
    resp2.encoding = 'gbk'
    result3 = ojb3.search(resp2.text)
    dic = result3.groupdict()
    writ.writerow(dic.values())#4、遍历写入文件
f.close()






























