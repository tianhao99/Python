# -*- coding: utf-8 -*-
"""
Created on Sun May 23 15:17:52 2021

@author: kingb
"""

import requests
from bs4 import BeautifulSoup
import csv

def pricepage (n):
    for i in range(n):
        url = f'http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml'
        resp = requests.get(url)
        resp.encoding = 'utf-8'
        f = open('菜价.csv',mode='a',encoding='utf-8')
        wri = csv.writer(f)
        
        
        page = BeautifulSoup(resp.text,'html.parser')#引号中表示指定html解析器，BeautifulSoup不用猜测，直接调用
        # pac = page.find(class_='hq_table')#class要加下划线，因为是Python中的关键字，避免冲突
        pac = page.find('table',attrs={'class':'hq_table'})#防止关键字冲突，直接定义一个字典放到字典中
        trlist = pac.find_all('tr')
        
        
        for tr in trlist:
            tds = tr.find_all('td')
            name = tds[0].text
            low = tds[1].text
            ave = tds[2].text
            high = tds[3].text
            gui = tds[4].text
            danwei = tds[5].text
            data = tds[6].text
            print([name,low,ave,high,gui,danwei,data])
            wri.writerow([name,low,ave,high,gui,danwei,data])
        f.close()       
        resp.close()

if __name__=='__main__':
    n = 100
    pricepage (n)


    
    
    
    
    
    
    
    
    
    
    
    
    
    