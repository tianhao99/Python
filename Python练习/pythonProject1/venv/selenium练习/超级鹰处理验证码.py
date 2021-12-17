

from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
import time
from chaojiying import Chaojiying_Client   #直接导入超级鹰的类

def senddata (user1,password1,imgtxt):
    web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys('13139313534')
    time.sleep(1)
    web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys(password1)
    time.sleep(1)
    web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(imgtxt,Keys.ENTER)
    time.sleep(1)
# saveimg函数：找到验证码图片位置，下载保存，返回图图片名称
# 但是这种形式会需要请求验证码图片位置，造成验证码刷新，不能使用！！！
# def saveimg():
#     address = web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/div/img').get_attribute('src')
#     # address = web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/div/img/@src')
#     img = requests.get(address)
#     img_name = address.split('=')[-1]+'.jpg'
#     with open(img_name,mode='wb') as f:
#         f.write(img.content)
#     f.close()
#     return img_name

#超级鹰处理


if __name__ == '__main__':
    url = 'http://www.chaojiying.com/user/login/'
    web = Chrome()
    web.get(url)
    # screenshot_as_png,对xpath位置进行屏幕截图，并保存为png格式，此时img是源码形式，不需要读操作，直接给超级鹰
    img = web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
    # 建立超级鹰对象
    chaojiying = Chaojiying_Client('13139313534', '13139313534', '918377')
    imgtxt = chaojiying.PostPic(img, 1004)['pic_str']
    senddata('1102899943@qq.com','SHAN153X',imgtxt)

