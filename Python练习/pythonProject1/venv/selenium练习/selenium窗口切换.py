

import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

web = Chrome()
web.get('http://www.lagou.com')

time.sleep(1)

web.find_element_by_xpath('//*[@id="changeCityBox"]/p[1]/a').click()

time.sleep(1)

web.find_element_by_xpath('//*[@id="search_input"]').send_keys('python',Keys.ENTER)

time.sleep(1)

web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[2]/div[1]/div[1]/div[1]/a/h3').click()

time.sleep(1)

# 获取第二页面中的信息
# 切换新的窗口视角，因为selenium中默认不跳转窗口
web.switch_to_window(web.window_handles[-1])        # 切换！！！
# 默认选 窗口选项卡中最后一个窗口，window.handles是选项卡列表，可直接索引

job_detail = web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]/div').text
print(job_detail)

# # 切换到iframe中
# #-----------------
# iframe123 = web.find_element_by_xpath('//*[@id="player_iframe"]') #先找到iframe
# web.switch_to.frame(iframe123)    #切换到iframe
# #开始操作，爬取等
# web.switch_to.default_content     #切换回原页面
# #-----------------