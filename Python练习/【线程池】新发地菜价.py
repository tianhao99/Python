# -*- coding: utf-8 -*-
"""
Created on Mon May 31 21:29:16 2021

@author: kingb
"""

import requests
from lxml import etree
import csv
from concurrent.futures import ThreadPoolExecutor
import time



f = open('【线程池新发地菜价】.csv',mode='w',encoding='utf-8')
wri = csv.writer(f)
def page_one(url):
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    temp = resp.text
    tree = etree.HTML(temp)   #转成对象，注意HTML和XML两种语言。
    #直接复制的xpath路径可能不正确，谷歌浏览器会默认增加某些标签，但网页源代码中没有，导致搜索失败！
    result = tree.xpath('/html/body/div[2]/div[4]/div[1]/table')[0]   #[0]否则是链表
    trs = result.xpath('./tr')[1:]  #不需要表头，从位置1开始取
    # trs = result.xpath('./tr[position()>1]')  #作用和上行一致，从位置1开始取
    for i in trs:
        txt = i.xpath('./td/text()')
        txt2 = (j.replace('\\','').replace('/','')for j in txt)   #替换文件中的\\和/，方便后期数据处理
        #生成器，其实就是简写的for循环
        wri.writerow(txt2)
    print('第%s页提取完毕！'%url.split('/')[-1].split('.')[0])#通过split函数分隔，取得包含在url中的页面数字


if __name__ == '__main__':
    t1 = time.time()
    with ThreadPoolExecutor(100) as t:
        for i in range(1,101):
            t.submit(page_one,f'http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml')
    print('over!')
    f.close()
    t2 = time.time()
    print(t2-t1)



