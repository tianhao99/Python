
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from chaojiying import Chaojiying_Client
from selenium.webdriver.chrome.options import Options
import time

# 13206中识别为自动化测试，登录失败解决
# 1、谷歌浏览器版本低于88
# web = Chrome()
# web.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#     "source": """
#                 navigator.webdriver = undefined
#                 Object.defineProperty(navigator,'webdriver', {
#                      get: () => undefined
#                 })
#             """
# })
# 2、谷歌浏览器版本大于等于88
option = Options()
option.add_experimental_option('excludeSwitches',['enable-automation']) # 可写可不写
option.add_argument('--disable-blink-features=AutomationControlled')


# 创建对象
web = Chrome(options=option) # 浏览器对象
chaojiying = Chaojiying_Client('13139313534', '13139313534', '918377') # 超级鹰对象

# 打开主页面
web.get('https://kyfw.12306.cn/otn/resources/login.html')
time.sleep(2)
web.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a').click()
time.sleep(3)

# 输入账号密码
web.find_element_by_xpath('//*[@id="J-userName"]').send_keys('888888888')
web.find_element_by_xpath('//*[@id="J-password"]').send_keys('888888888')
time.sleep(2)

# 处理验证码

# 找到验证码图片
img_base = web.find_element_by_xpath('//*[@id="J-loginImg"]')
coordinate = chaojiying.PostPic(img_base.screenshot_as_png,9004)['pic_str'] #将验证码截图传给超级鹰，返回坐标
# 9004-->坐标多选,返回1~4个坐标,如:x1,y1|x2,y2|x3,y3
# 字典中'pic_str'为返回的验证码必要信息，此处返回坐标点
coordinate_list = coordinate.split('|')
for i in coordinate_list:
    x_x = int(i.split(',')[0])   #此时虽然拆分出坐标，但是是'字符串'格式，需加int转换成  数值。
    y_y = int(i.split(',')[1])
    ActionChains(web).move_to_element_with_offset(img_base,x_x,y_y).click().perform()
    # move_to_element 移动鼠标到此前找到的element位置，如img_base
    # with_offset    移动到位置之后，以该位置顶点为原点，建立坐标系，通过x，y偏移量 移动鼠标到 精确位置
    # ActionChains.......一系列定义了一个事件链，如何操作，最后perform表示执行，不加perform，即使有click也不会点击
time.sleep(5)

# 点击登陆
web.find_element_by_xpath('//*[@id="J-login"]').click()

time.sleep(5)  # 必须要睡会，还要睡够，要不然找不到界面直接报错

# 解决滑块验证
button = web.find_element_by_xpath('//*[@id="nc_1_n1z"]')
ActionChains(web).drag_and_drop_by_offset(button,300,0).perform()
# 事件链操作，拖拽在x,y坐标系中，以button为顶点建立坐标系，长度用截图工具可直观看到