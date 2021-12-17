

#主要是拼接地址
#1、拿到主页面源代码，获得iframe
#2、从iframe的页面源代码中找到第一个m3u8文件
#3、从第一个m3u8文件中筛出第二个m3u8文件
#4、下载视频
#5、下载后的ts文件，不能播放
import requests
from bs4 import BeautifulSoup
import re
import asyncio
import aiohttp
import aiofiles
from Crypto.Cipher import AES
import os

def get_key(url):#获取密钥
    resp = requests.get(url)
    resp.encoding='utf-8'
    key = resp.text
    resp.close()
    return key

async def dec_ts(name, key):#解密
    aes = AES.new(key=key,IV=b"0000000000000000", mode=AES.MODE_CBC)#偏移量IV有就写，没有就写0，位数根据密钥位数而定
    async with aiofiles.open("视频大合集" + "/" + name, mode="rb") as f1, aiofiles.open("视频大合集" + "/" + "tmp_" + name, mode="wb") as f2:
        bs = await f1.read()
        await f2.write(aes.decrypt(bs))
        print(f"{name}~解密OK~")

async def aio_dec(key):
    tasks = []
    async with aiofiles.open("最终m3u8文件.txt", mode="r", encoding="utf-8") as f:
        async for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()
            tasks.append(dec_ts(line, key))
    # 异步解密
        await asyncio.wait(tasks)

def merge_ts():#合并所有ts文件为一个
    s = []
    with open("最终m3u8文件.txt") as f:
        for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()
            s.append("./视频大合集/tmp_"+line)
    names = "+".join(s)
    os.system(f"copy{names} movie.mp4")

async def aio_download_ts(url,name,session):
    async with session.get(url_2) as resp:
        async with aiofiles.open(f'视频大合集/+{name}',mode='wb',encoding='utf-8') as f:
            await f.write(await resp.content.read())

async def aio_download_find(url):
    tasks = []
    async with aiohttp.ClientSession() as session:
        async with aiofiles.open('最终m3u8文件.txt', mode='r', encoding='utf-8') as f:
            # 文件里面内容格式如下，一行#一行地址：
            #   #EXTM3U
            #   dsaf15651315.ts
            #   #EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=924000,RESOLUTION=1024×576
            #   gerg51616881.ts
            async for line in f:
                if line.startswith('#'):
                    continue
                else:
                    line = line.strip()  # 删除换行符和前后空格
                    # https://boba.52kuyun.com/20170906/Moh2l9zV/hls/index.m3u8
                    # line: dsaf15651315.m3u8
                    # 目标：https://boba.52kuyun.com/20170906/Moh2l9zV/hls/dsaf15651315.m3u8，直接拼接
                    url_2 = url+line
                    task = asyncio.create_task(aio_download_ts(url_2,line,session))#直接在这里定义session，传参过去
                    tasks.append(task)
            await asyncio.wait(tasks)

def download_m3u8_file(url,name):
    resp = requests.get(url)
    with open(name,mode='wb') as f:
        f.write(resp.content)
    print("第一个m3u8文件下载完成！！！")

def get_first_m3u8(url):
    # resp = requests.get(url)
    # rex = re.compile(r'var main = "(?p<url_m3u8>.*?)"',re.S)
    # url_m3u8 = rex.search(resp.text).group('url_m3u8')
    # return url_m3u8
    return '/20170906/Moh2l9zV/index.m3u8?sign=548ae366a075f0f9e7c76af215aa18e1' #替换代码，网站正常应该运行上边四行代码
    # /20170906/Moh2l9zV/index.m3u8?sign=548ae366a075f0f9e7c76af215aa18e1   #网站崩了，只能手打出来

def get_iframe(url):
    resp_iframe = requests.get(url)
    main_page = BeautifulSoup(resp_iframe.text,'html.parser')
    src = main_page.find('iframe').get('src')   #寻找iframe标签，获得src属性值
    return src

def main(url):
    #1、拿到主页面代码
    iframe_src = get_iframe(url)
    # iframe_src:   https://boba.52kuyun.com/share/xfPs9NPHvYGhNzFp
    #2、拿第一个源码中的m3u8文件
    url_first_m3u8_1 = get_first_m3u8(iframe_src)  #需要拼接
    # url_first_m3u8_1: /20170906/Moh2l9zV/index.m3u8?sign=548ae366a075f0f9e7c76af215aa18e1
    page_one = iframe_src.split('/share')[0]#分隔,取0，
    # page_one = iframe_src.split('/',2)[0]#从右侧开始用/切割，切割2次，取0，
    url_first_m3u8 = page_one+url_first_m3u8_1
    # 组合后的地址： https://boba.52kuyun.com/20170906/Moh2l9zV/index.m3u8?sign=548ae366a075f0f9e7c76af215aa18e1
    #3.1、下载第一个m3u8文件
    download_m3u8_file(url_first_m3u8,'file_first_m3u8.txt')
    #3.2、读取第一个m3u8文件内容，获得最终拼接地址
    with open('file_first_m3u8.txt',mode='r',encoding='utf-8') as f:
        #文件里面内容如下：
        #   #EXTM3U
        #   #EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=924000,RESOLUTION=1024×576
        #   hls/index.m3u8
        for line in f:
            if line.startswith('#'):
                continue
            else:
                line = line.strip()#删除换行符和前后空格   line:  hls/index.m3u8
                url_second_m3u8_1 = url_first_m3u8.split('index')[0]
                # https://boba.52kuyun.com/20170906/Moh2l9zV/index.m3u8?sign=548ae366a075f0f9e7c76af215aa18e1
                #切割后：https://boba.52kuyun.com/20170906/Moh2l9zV/
                url_second_m3u8 = url_second_m3u8_1+line
                #组合后：https://boba.52kuyun.com/20170906/Moh2l9zV/hls/index.m3u8
    #3.3、已有视频地址，开始下载m3u8文件
    download_m3u8_file(url_second_m3u8,'最终m3u8文件.txt')
    #4、读取最终m3u8文件，异步开始下载
    # https://boba.52kuyun.com/20170906/Moh2l9zV/hls/index.m3u8
    # line: dsaf15651315.m3u8
    # 目标：https://boba.52kuyun.com/20170906/Moh2l9zV/hls/dsaf15651315.m3u8，直接用下面replace()替换掉末尾'index.m3u8'，剩余直接传参给函数，函数里面直接拼接
    url_second_m3u8_2 = url_second_m3u8.replace('index.m3u8','')

    asyncio.run(aio_download_find(url_second_m3u8_2))
if __name__ == '__main__':
    url = 'https://www.91kanju.com/vod-play/541-2-1.html'
    main(url)

