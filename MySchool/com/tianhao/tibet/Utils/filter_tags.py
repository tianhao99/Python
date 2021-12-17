import re
import requests


#过滤HTML中的标签

# 将HTML中标签等信息去掉
# @param htmlstr HTML字符串.
from com.tianhao.tibet.Utils.replaceCharEntity import replaceCharEntity


def filter_tags(htmlstr):
    # 先过滤CDATA
    re_cdata = re.compile('//<!\[CDATA\[[^>]*//\]\]>', re.I)  # 匹配CDATA
    re_script = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)  # Script
    re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>', re.I)  # style
    re_br = re.compile('<br\s*?/?>')  # 处理换行
    re_h = re.compile('</?\w+[^>]*>')  # HTML标签
    re_comment = re.compile('<!--[^>]*-->')  # HTML注释
    s = re_cdata.sub('', htmlstr)  # 去掉CDATA
    s = re_script.sub('', s)  # 去掉SCRIPT
    s = re_style.sub('', s)  # 去掉style
    s = re_br.sub('\n', s)  # 将br转换为换行
    s = re_h.sub('', s)  # 去掉HTML 标签
    s = re_comment.sub('', s)  # 去掉HTML注释
    # 去掉多余的空行
    blank_line = re.compile('\n+')
    s = blank_line.sub('\n', s)
    s = replaceCharEntity(s)  # 替换实体
    return s
if __name__ == '__main__':
    url = 'http://tb.tibet.cn/tb/people/201810/t20181010_6311049.html'
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    data = resp.text

    # 取出大范围文件
    partten_text = re.compile(r'<div class="center">(.*?)<div class="manu">', re.S)
    rexdata_1 = partten_text.search(data).group(0)
    rexdata =filter_tags(rexdata_1)
    print(rexdata)