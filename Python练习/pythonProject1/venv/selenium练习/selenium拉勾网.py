from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys    #获得伪键盘操作，如enter
import time

web = Chrome()
web.get('https://www.lagou.com')  #进入网页

el = web.find_element_by_xpath('//*[@id="changeCityBox"]/p[1]/a')
el.click()
time.sleep(1)

web.find_element_by_xpath('//*[@id="search_input"]').send_keys('Python',Keys.ENTER)
#xpath找到搜索框，send_keys发送搜索内容，同时携带Keys.ENTER，输入完成直接回车
# 也可以重复上边操作，xpath找到‘搜索’，通过click（）点击

# li_list = web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[1]')
li_list = web.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li')#复制过来的li[1],要获得的是所有li，去掉末尾的[1]
#注意！！！这里用的elements，多了一个s，表示查找所有，element表示 查找第一个就停止
for li in li_list:
    job_name = li.find_element_by_tag_name('h3').text  #tag_name标签名
    job_price = li.find_element_by_xpath('./div[1]/div[1]/div[2]/div/span').text
    company = li.find_element_by_xpath('./div[1]/div[2]/div[1]/a').text
    base = li.find_element_by_tag_name('em').text
    need = li.find_element_by_xpath('./div[1]/div[1]/div[2]/div').text
    print(company,job_name,job_price,need,base)


