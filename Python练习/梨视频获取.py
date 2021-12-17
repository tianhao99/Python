# -*- coding: utf-8 -*-
"""
Created on Fri May 28 10:26:17 2021

@author: kingb
"""

import requests

url = 'https://www.pearvideo.com/video_1727354'

contId = url.split('_')[-1]                     #取得网址的末尾数字，用于拼接下载地址
videourl = f'https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.3126890921325589'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Referer': url                              #追溯上一层网页，防盗链
    }

resp = requests.get(videourl,headers=header)    #取得拼接视频下载地址所需的字典内容
dic = resp.json()
systemTime = dic['systemTime']
srcurl = dic['videoInfo']['videos']['srcUrl']    
w = srcurl.replace(systemTime,'cont-'+contId)    #拼接视频的下载地址

w1 = requests.get(w)        #获取视频的下载地址
with open(f'{contId}.mp4',mode='wb') as f: 
    f.write(w1.content)            #写入文件     w1.content是视频的字节---解码
    print('over!!!')            #写入一个，输出一个over表示结束
f.close()








