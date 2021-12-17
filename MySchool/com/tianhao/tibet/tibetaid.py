
import re
import requests
import threading
from com.tianhao.tibet.Utils.filter_tags import filter_tags


def getContent(url, title, file):

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
        print(url)
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
            if it.group(1).split(':')[0] == 'http':
                continue
            # elif it.group(1).split('sta')[0] == '../':
            #     url_content = "http://tb.tibet.cn/tb/law/" + it.group(1).split('../')[-1]
            elif it.group(1).split('coun')[0] == '../':
                url_content = "http://tb.tibet.cn/tb/aid_tibet/" + it.group(1).split('../')[-1]
            elif it.group(1).split('index')[0] == '../../':
                url_content = 'http://tb.tibet.cn/tb/' + it.group(1).split('../../')[-1]
            else:
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

    # 1、对口支援【ཁ་བཏད་རོགས་སྐྱོར།】
    url = 'http://tb.tibet.cn/tb/aid_tibet/counterpart/'
    urls = []
    urls.append(url)
    for i in range(1,9):
        urls.append(f'{url}index_{i}.html')

    # 确定文件写入位置：相对路径
    file = 'བོད་སྐྱོར།/ཁ་བཏད་རོགས་སྐྱོར།'
    getTitleAndUrl(urls,file)


    # 2、援助协会【རོགས་སྐྱོར་མཐུན་ཚོགས།】
    url = 'http://tb.tibet.cn/tb/aid_tibet/group/'
    urls = []
    urls.append(url)
    for i in range(1,3):
        urls.append(f'{url}index_{i}.html')

    # 确定文件写入位置：相对路径
    file = 'བོད་སྐྱོར།/རོགས་སྐྱོར་མཐུན་ཚོགས།'
    getTitleAndUrl(urls,file)


    # 3、援藏故事【བོད་སྐྱོར་གཏམ་རྒྱུད།】
    url = 'http://tb.tibet.cn/tb/aid_tibet/story/'
    pages = 3


    urls = []
    urls.append(url)
    for i in range(1,pages):
        urls.append(f'{url}index_{i}.html')

    # 确定文件写入位置：相对路径
    file = 'བོད་སྐྱོར།/བོད་སྐྱོར་གཏམ་རྒྱུད།'
    getTitleAndUrl(urls,file)
