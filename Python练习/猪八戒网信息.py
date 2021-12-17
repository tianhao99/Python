# -*- coding: utf-8 -*-
"""
Created on Thu May 27 17:28:00 2021

@author: kingb
"""

#自己写的
#1、获得代码
#2、提取信息：需求、店名、城市、价格、交易数量

import requests
from lxml import etree
import csv


url = 'https://beijing.zbj.com/search/f/?type=new&kw=saas'
page = requests.get(url)
page.encoding = 'utf-8'

f = open('猪八戒.csv',mode='a',encoding='utf-8')
wri = csv.writer(f)

tree = etree.HTML(page.text)
pageall = tree.xpath('/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div')
# =============================================================================
# pageall = tree.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div[1]/*[@class='item-wrap service-new j-sp-item-wrap  ']")
# #同理也是剔除广告，因为广告的class值不同，可以在生成列表时用class不用div，div无法区分广告信息，
# #若用div，在后边遍历时增加if，判断是否为广告
# =============================================================================
j = 0
for i in pageall:
    if i.xpath('./@class')[0] == 'item-wrap service-new j-sp-item-wrap  ':   #剔除广告页面
        xuqiu = 'saas'.join(i.xpath('./div/div/a[1]/div[2]/div[2]/p/text()'))
        dname = i.xpath('./div/div/a[2]/div[1]/p/text()')[0]
        city = i.xpath('./div/div/a[2]/div[1]/div/span/@title')[0]
        price = i.xpath('./div/div/a[1]/div[2]/div[1]/span[1]/text()')[0].strip('¥')
        count = i.xpath('./div/div/a[1]/div[2]/div[1]/span[2]/text()')[0]
        wri.writerow([xuqiu,dname,city,price,count])
        j+=1
        print(f'over{j}')
print('over all!')
f.close()








