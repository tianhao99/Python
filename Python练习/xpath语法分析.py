# -*- coding: utf-8 -*-
"""
Created on Thu May 27 00:02:41 2021

@author: kingb
"""
from lxml import etree

# =============================================================================
# temp = '''    代码    '''
# tree = etree.XML(temp)   #转成对象
# result = tree.xpath('/根节点')   #/表示层级关系，第一个/是根节点
# result = tree.xpath('/根节点/子目标节点')   
# result = tree.xpath('/根节点/子目标节点/text()')   #text()表示拿子节点中的文本信息
# result = tree.xpath('/根节点/子节点//子子目标节点text()')    #‘//’两个表示所有后代
# result = tree.xpath('/根节点/子节点/*/子子目标节点text()')   #‘*’是通配符，取子节点下的任意目标
# result = tree.xpath('/根节点/子节点/目标节点[2]/text()')   #几个相同名字的目标节点，可直接中括号＋索引，默认从1开始
# result = tree.xpath('/根节点/子节点/目标节点[@href='属性值']/text())   #目标节点中括号＋@属性名字，可直接获得该属性的text
# result = tree.xpath('/根节点/子节点/几个相同的目标节点)  #此时result是一个列表，保存了几个相同节点，可直接遍历
# =============================================================================
# #遍历
# for i in result:
#     #从每一个li中提取到文字信息
#     result1 = i.xpath('./i中的第一个子节点/子子节点/目标节点/text()')    #相对根节点中必须前面有一个‘./’，只有绝对根节点才可以直接用/
#     #获得某个标签的属性值如：href、id、class之类的，直接@
#     result2 = i.xpath('./i中的第一个子节点/子子节点/目标节点/@href')
# =============================================================================
    


 

# =============================================================================
