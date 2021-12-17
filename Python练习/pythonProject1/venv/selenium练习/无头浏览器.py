
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select   # 处理下拉菜单
from selenium.webdriver.chrome.options import Options  # 无头浏览器
import time
import csv

# 无头浏览器
# 准备好配置参数
opt = Options()
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')

web = Chrome(options=opt)  # 无头浏览器对象
# web = Chrome()           # 普通对象

web.get('https://www.endata.com.cn/BoxOffice/BO/Year/index.html')

# 先定位到下拉菜单
sel_element = web.find_element_by_xpath('//*[@id="OptionDate"]')
# 对元素进行包装
sel = Select(sel_element)
# 让浏览器进行调整选项
for i in range(len(sel.options)):
    # 三种查找方法，<option value="2021">2021年</option>
    # index()用列表的索引，value()用属性值更换，visible_text()用菜单中的文本更换
    sel.select_by_index(i)          #本例中索引值
    # sel.select_by_value()         #本例中2021
    # sel.select_by_visible_text()  #本例中2021年
    time.sleep(1)
    tbody_list = []
    print(i)
    #开始抓取数据
    table123 = web.find_element_by_xpath('//*[@id="TableList"]/table')
    tbody_list = table123.find_elements_by_xpath('./tbody/tr') # element只查找第一个，elements查找多个，形成列表
    for j in tbody_list:
        name = j.find_element_by_xpath('./td[2]/a/p').text
        type = j.find_element_by_xpath('./td[3]').text
        box_office = j.find_element_by_xpath('./td[4]').text
        country = j.find_element_by_xpath('./td[7]').text
        date = j.find_element_by_xpath('./td[8]').text
        years = web.find_element_by_xpath(f'//*[@id="OptionDate"]/option[{i+1}]').text
        f =  open('票房数据/'+f'{years}票房数据.csv',mode='a',encoding = 'utf-8')
        wri = csv.writer(f)
        wri.writerow([name,type,box_office,country,date])
web.page_source
f.close()
web.close()