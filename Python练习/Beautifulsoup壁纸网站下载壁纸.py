# -*- coding: utf-8 -*-
"""
Created on Sun May 23 21:42:28 2021

@author: kingb
"""

#1、获取网页源代码并取得跳转链接
#2、获取子页面源代码
#3、获取图片下载地址
#4、存入文件

import requests
from bs4 import BeautifulSoup as bs
import time


# 1、获取首页main_page源代码
# url = 'https://www.umei.net/bizhitupian/meinvbizhi/'
url = 'https://www.umei.net/weimeitupian/'
resp_main = requests.get(url)
resp_main.encoding = 'utf-8'

#把源代码交给BeautifulSoup,并告知为html格式
main_page = bs(resp_main.text,'html.parser')

main_list = main_page.find('div',class_='TypeList')
href_list = main_list.find_all('a',class_='TypeBigPics')
for li in href_list:
    href = li.get('href')
    
    # 2、获取子页面second_page源代码
    url_second = 'https://www.umei.net'+href
    resp_second = requests.get(url_second)
    resp_second.encoding = 'utf-8'
    #子页面源代码交给BeautifulSoup,并告知为html格式
    second_page = bs(resp_second.text,'html.parser')
    
    #3获取图片下载地址
    second_list = second_page.find('p',align='center')
    src = second_list.find('img').get('src')
    img = requests.get(src)   #下载图片
    #4、存入文件
    img_name = src.split('/')[-1]   #拿到http://c8e.jpg中最后一个下划线以后的内容，为每一个图片命名
    with open('bizhi/'+img_name,mode='wb') as f:
        #img.content是图片的字节---解码
        f.write(img.content)        #图片写入文件
    print('over!!!',img)
    f.close()
    resp_second.close()
    time.sleep(1)
print('all over')
resp_main.close()



















