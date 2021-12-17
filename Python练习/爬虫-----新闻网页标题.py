# -*- coding: utf-8 -*-
"""
Created on Thu May 13 19:39:35 2021

@author: kingb
"""
#                          网页爬取新闻标题
import re
import requests
from urllib.parse import quote #导入quote方法对URL中的字符进行编码
class BaiduNewsCrawler: #定义BaiduNewsCrawler类
    headersParameters = { #发送HTTP请求时的HEAD信息
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 
		  'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 
	  	'Mozilla/6.1 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    }
    def __init__(self, keyword, timeout): #定义构造方法
        self.url='https://news.baidu.com/ns?word='+ quote(keyword) + '&tn=news&from=news&cl=2&rn=20&ct=1' #要爬取的新闻网址
        self.timeout=timeout #连接超时时间设置（单位：秒）
    def GetHtml(self): #定义GetHtml方法
        request=requests.get(self.url, timeout=self.timeout, headers=self.headersParameters)      #根据指定网址爬取网页
        self.html=request.text #获取新闻网页内容
    def GetTitles(self): #定义GetTitles方法
        self.titles = re.findall(r'<h3 class="c-title">([\s\S]*?)</h3>',self.html)   #匹配新闻标题
        for i in range(len(self.titles)):       #对于每一个标题
            self.titles[i]=re.sub(r'<[^>]+>','',self.titles[i])      #去除所有HTML标记，即<...> 
            self.titles[i]=self.titles[i].strip()       #将标题两边的空白符去掉
    def PrintTitles(self): #定义PrintTitle方法
        no=1
        for title in self.titles: #输出标题
            print(str(no)+':'+title)
            no+=1
if __name__ == '__main__':
    bnc = BaiduNewsCrawler('西藏大学',30) #创建BaiduNewsCrawler类对象
    bnc.GetHtml() #获取新闻网页的内容
    bnc.GetTitles() #获取新闻标题
    bnc.PrintTitles() #输出新闻标题