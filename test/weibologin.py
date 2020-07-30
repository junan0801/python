import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import execjs
# 这个是一个用来控制chrome以无界面模式打开的浏览器
# 创建一个参数对象，用来控制chrome以无界面的方式打开
chrome_options = Options()
# 后面的两个是固定写法 必须这么写
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--windows-size=920*180')

chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--hide-scrollbars')
# 驱动路径 谷歌的驱动存放路径
path = r'C:\Users\mx-0123\AppData\Local\Google\Chrome\Application\chromedriver.exe'
# 创建浏览器对象
browser = webdriver.Chrome(executable_path=path, options=chrome_options)
url = 'https://weibo.com/login'
browser.get(url)
time.sleep(2)
browser.find_element_by_id('loginname').clear()
browser.find_element_by_id('loginname').send_keys('656540580@qq.com')
browser.find_element_by_name('password').clear()
browser.find_element_by_name('password').send_keys('Jun0801weibo')
browser.find_element_by_class_name('W_btn_a btn_32px').click()
time.sleep(15)
#browser.switch_to.frame('treelist')
#browser.execute_script("javascript:f_select('C33', '', '')")
#browser.switch_to.parent_frame()
#browser.switch_to.frame('da')
#t = browser.find_element_by_id('pageTitle').text
#print('t=', t)
#time.sleep(5)
#
#
## 切换到指定frame后执行注销功能
#browser.switch_to.default_content()
#browser.switch_to.frame('globalnav')
#browser.execute_script('javascript:f_logout();')
browser.quit()