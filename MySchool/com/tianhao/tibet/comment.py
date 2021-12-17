
import re
import requests
import threading

def getContent(url,title,file):
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    }

    resp = requests.get(url,headers=headers)
    resp.encoding = 'utf-8'
    data = resp.text


    # 获取正文   正则表达式
    partten_text =re.compile(r'<font style=.*?>(?P<text_new>.*?)<',re.S)
    # 获取文本 迭代器
    rexdata = partten_text.finditer(data)

    with open(f'../news/tbtibetcn/{file}/{title}.txt', mode='a',encoding='utf-8') as f:
        f.write(title+ '\r\n'+ '\r\n')
        for it in rexdata:
            txt = it.group('text_new').strip().strip('&nbsp; ').strip('<b>')
            f.write(txt.replace('&nbsp;','') + '\r\n')
    f.close()

def getTitleAndUrl(urls,file):

    # 获取标题 和  正文的url           正则表达式对象
    parttern_title_url = re.compile(r'<dt><a href="(.*?)" target="_blank">(.*?)</a>', re.S)

    # 遍历取出所有的title和url
    for url in urls:
        resp = requests.get(url)
        resp.encoding = 'utf-8'
        data = resp.text
        #利用正则筛选目标对象
        data_title_url = parttern_title_url.finditer(data)

        threads = []
        for it in  data_title_url:
            # 取出title和url
            url_content = urls[0] + it.group(1).split('./')[-1]

            # 用标题命名文件，替换不能用于文件名的特殊字符，换成_下划线
            rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
            title = re.sub(rstr, "_", it.group(2)).strip()  # 替换为下划线

            # 调用getContent方法，获取文本并写入文件【多线程】
            threads.append(threading.Thread(target=getContent,args=(url_content,title,file)))
            # getContent(url_content,title,file)
        for thread in threads:
            thread.start()

        print(f'{url}页面完成')

if __name__ == '__main__':
    # 确定首页网址
    urls = ['http://tb.tibet.cn/tb/review/']
    for i in range(1,20):
        urls.append(f'http://tb.tibet.cn/tb/review/index_{i}.html')
    # 确定文件写入位置：相对路径
    file = 'དཔྱད་གཏམ།'
    getTitleAndUrl(urls,file)
