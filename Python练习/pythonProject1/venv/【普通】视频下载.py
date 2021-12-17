

import requests
import re

url = 'https://www.91kanju.com/vod-play/54812-1-1.html'
resp = requests.get(url)
rex = re.compile(r".*?const dp = new DPlayer.*?url: '(?P<url1>.*?)',.*?type: 'customHls'",re.S)
result = rex.search(resp.text)
url_m3u8 = result.group('url1')
m3u8_txt = requests.get(url_m3u8)
with open ('视频.m3u8',mode='wb') as f:
    f.write(m3u8_txt.content)
m3u8_txt.close()
#写入程序之后，开始操作，此时不需要前边的代码。
n = 1
with open ('视频.m3u8',mode='r',encoding='utf-8') as f:
    for line in f:
        line = line.strip()#先去掉每行前后的空格，换行符
        if line.startswith('#'):#如果开头为#就跳过，因为开头为#的不是我们要的下载地址
            continue
        download = requests.get(line)
        f = open(f'video/{n}.ts',mode='wb')
        f.write(download.content)
        f.close()
        download.close()
        print('完成%d个' %n)
        n+=1
    print('全部完成！！')

