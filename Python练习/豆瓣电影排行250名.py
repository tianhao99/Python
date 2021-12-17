# -*- coding: utf-8 -*-
"""
Created on Thu May 20 14:53:49 2021

@author: kingb
"""
#豆瓣前250电影排名

import requests
import re
import csv


def pageonce (url):
    header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
    data1 = requests.get(url,headers=header)
    page_data = data1.text
    #print(data1.status_code)检验前边代码
    
    rex =re.compile(r'<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<div class="star">.*?<span class="rating_num" property="v:average">(?P<count>.*?)</span>.*?<span property="v:best" content="10.0"></span>.*?<span>(?P<people>.*?)人评价</span>',re.S)
    rexdata = rex.finditer(page_data)
    f = open('data.csv',mode='a')
    csvwr = csv.writer(f)
    j = 1
    dic = {}
    for it in rexdata:
        print(j)
        print('剧名：%s'%it.group('name'))
        print('年份：%s'%it.group('year').strip())
        print('评分：%s'%it.group('count'))
        print('评分人数：%s'%it.group('people'))
        dic = it.groupdict()
        dic['year'] = dic['year'].strip()
        csvwr.writerow(dic.values())
        j +=1

f = open('data.csv',mode='w')
f.truncate()
for i in range(0,250,25):
    url222 = f"https://movie.douban.com/top250?start={i}"
    pageonce (url222)
f.close()  
    
    
    
    
    
    
    
    
    
    
    
    