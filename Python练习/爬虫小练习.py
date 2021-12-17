# -*- coding: utf-8 -*-
"""
Created on Fri May 14 22:02:08 2021

@author: kingb
"""
#print(r.status_code)
#伪装浏览器访问
import requests
url = "https://www.amazon.com/-/zh/dp/B079JLY5M5/ref=sr_1_2?dchild=1&fst=as%3Aoff&pf_rd_i=16225007011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=55ca1a29-07df-438e-9133-82fa08d479b7&pf_rd_r=TN3QTE0YXWYFHBKC68V3&pf_rd_s=merchandised-search-4&pf_rd_t=101&qid=1621005981&rnid=16225007011&s=computers-intl-ship&sr=1-2"
try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url,headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败")
#%%    模拟搜索引擎
import requests
keyword = 'Python'
try:
    kv = {'wd':keyword}
    hd = {'user-agent':'Mozilla/5.0'}
    r = requests.get('http://www.baidu.com/s',params = kv,headers = hd)
    print(r.request.url)
    r.rasie_for_status()
    print(len(r.text))
except:
    print('爬取失败')
    
#%%图片抓取保存/////失败///////////
import requests
import os
url = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fs9.sinaimg.cn%2Fmw690%2F0075yGppzy7mWIXRo4o78%26690&refer=http%3A%2F%2Fs9.sinaimg.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1623632914&t=4e404c284fa841b61851d98df640981e'
root = 'D://picss//'
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open (path,'wb') as f:
            f.write(r.conten)
            f.close()
            print('文件保存成功 ')
    else:
        print('文件已存在')
except:
    print('爬取失败')
#%%























