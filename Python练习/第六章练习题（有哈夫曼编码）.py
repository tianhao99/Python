# -*- coding: utf-8 -*-
"""
Created on Thu May 13 21:05:54 2021

@author: kingb
"""


    
#%% 第六章正则表达式

import re
urls = []
content = str(input())
pttn = r'(<a href="[\s\S]*?")'
pttn2 = r'["](.*?)["]'#正则表达式中[]表示里面的是特殊符号，不是字符串开头
urls = re.findall(pttn,content)
urls2 = re.findall(pttn2,str(urls))
for url in urls2:
    print(url)
#%%第六章填空题
class Time:
    def __init__(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second
t=Time(8,1,25)
str1='{0.hour}:{0.minute}:{0.second}'
str2='{t.hour}:{t.minute}:{t.second}'
print(str1.format(t))
print(str2.format(t=t))
#%%
import re   #compile函数将正则表达式转化为正则表达式对象
pattern=re.compile(r'<[^<]*>')     #调用方式由re.match/search(pattern,str),变成：pattern.match(str）
result=pattern.match('<h1>Nankai University</h1>')
print('content:%s,beg:%d,end:%d'%(result.group(),result.start(),result.end()))
#%%
import re 
s1 = str(input())
s2 = str(input())
if s1.find(s2) != -1:
    i = s1.find(s2) 
    print(i)     
while i != -1:
     i = s1.find(s2,i+1)
     if i != -1:
         print(i)
#%%          
s1 =input()   
m = 0
s2 = s1.split()     #split   将一个字符串分割成多个字符串，分隔符默认为空格，split(sep,num)分隔符、分割次数
for i in s2:
     m = m + eval(i)
print(m)
#%%     哈夫曼编码
s1 = []
n = eval(input())
for i in range(n):
    s1.append(input())

s1.sort(reverse=False)
print(s1)
for i in range(n-1):
    if s1[i+1].find(s1[i])==0:
        print('invalid')
        break
else:
    print('valid') 








           
            
            
            