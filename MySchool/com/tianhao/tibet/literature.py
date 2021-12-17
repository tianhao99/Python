
import re
import requests
import threading
from com.tianhao.tibet.Utils.filter_tags import filter_tags


def getContent(url, title, file):
    i = 0
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    }

    resp = requests.get(url,headers=headers)
    resp.encoding = 'utf-8'
    data = resp.text
    # 正则，取出文本块内容
    partten = re.compile(r'<div class="center">(.*?)<div class="manu">', re.S)

    try:
        rexdata_1 = partten.search(data).group(0)
    except:
        i = i + 1
        print(i)
        pass

    # 去除所有html标签  css标签内容   特殊字符的转换&nbsp 换成空格
    rexdata = filter_tags(rexdata_1)


    with open(f'../news/tbtibetcn/{file}/{title}.txt', mode='a',encoding='utf-8') as f:
        # 写入标题
        f.write(title + '\r\n')
        # 写入文章
        f.write(rexdata.strip())
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
    # 1、历史【ལོ་རྒྱུས།】
    urls = ['http://tb.tibet.cn/tb/literature/ls/']
    for i in range(1,20):
        urls.append(f'http://tb.tibet.cn/tb/literature/ls/index_{i}.html')

    # 确定文件写入位置：相对路径
    file = 'རྩོམ་རིག/ལོ་རྒྱུས།'
    getTitleAndUrl(urls,file)


    # 2、故事【སྒྲུང་གཏམ།】
    urls = ['http://tb.tibet.cn/tb/literature/xs/']
    for i in range(1,2):
        urls.append(f'http://tb.tibet.cn/tb/literature/xs/index_{i}.html')

    # 确定文件写入位置：相对路径
    file = 'རྩོམ་རིག/སྒྲུང་གཏམ།'
    getTitleAndUrl(urls,file)


    # 3、诗歌【སྙན་ངག】
    urls = ['http://tb.tibet.cn/tb/literature/sg/']
    for i in range(1,14):
        urls.append(f'http://tb.tibet.cn/tb/literature/sg/index_{i}.html')

    # 确定文件写入位置：相对路径
    file = 'རྩོམ་རིག/སྙན་ངག'
    getTitleAndUrl(urls,file)


    # 4、散文【ལྷུག་རྩོམ།】
    urls = ['http://tb.tibet.cn/tb/literature/sw/']
    for i in range(1,5):
        urls.append(f'http://tb.tibet.cn/tb/literature/sw/index_{i}.html')

    # 确定文件写入位置：相对路径
    file = 'རྩོམ་རིག/ལྷུག་རྩོམ།'
    getTitleAndUrl(urls,file)


    # 5、译著【བསྒྱུར་རྩོམ།】
    urls = ['http://tb.tibet.cn/tb/literature/yw/']
    # for i in range(1,20):
    #     urls.append(f'http://tb.tibet.cn/tb/literature/ls/index_{i}.html')

    # 确定文件写入位置：相对路径
    file = 'རྩོམ་རིག/བསྒྱུར་རྩོམ།'
    getTitleAndUrl(urls,file)


    # 6、论文【དཔྱད་རྩོམ།】
    urls = ['http://tb.tibet.cn/tb/literature/lw/']
    for i in range(1,20):
        urls.append(f'http://tb.tibet.cn/tb/literature/lw/index_{i}.html')

    # 确定文件写入位置：相对路径
    file = 'རྩོམ་རིག/དཔྱད་རྩོམ།'
    getTitleAndUrl(urls,file)

