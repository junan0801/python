import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
nu = -352
# 这个是一个用来控制chrome以无界面模式打开的浏览器
# 创建一个参数对象，用来控制chrome以无界面的方式打开
chrome_options = Options()
# 后面的两个是固定写法 必须这么写
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--windows-size=1920*1080')
# chrome_options.add_argument('--hide-scrollbars')
# 驱动路径 谷歌的驱动存放路径
path = r'C:\Users\mx-0123\AppData\Local\Google\Chrome\Application\chromedriver.exe'
# 创建浏览器对象
browser = webdriver.Chrome(executable_path=path, options=chrome_options)
url = 'https://mxops.imoxiu.cn/mxserver/asset/list/'
browser.get(url)
# browser.find_element_by_name('username').clear()
browser.find_element_by_name('username').send_keys('sysop')
# browser.find_element_by_name('password').clear()
browser.find_element_by_name('password').send_keys('Mo1991!xiU')
browser.find_element_by_tag_name('button').click()
time.sleep(5)
browser.find_element_by_id('search_input').send_keys(nu)
browser.find_element_by_id('search_btn').click()
time.sleep(5)
url = 'https://mxops.imoxiu.cn/mxserver/asset/list/?idc_id=0&rack_id=0&asset_type=&status=&keyword='+str(nu)
browser.get(url)
browser.find_element_by_xpath('/html/body/div[2]/div[1]/section[2]/div/div/div/div[2]/form/table/tbody/tr/td[1]/a[1]').click()
sn = browser.find_element_by_xpath('/html/body/div[2]/div/section[2]/div/div/div/div/div[1]/table/tbody/tr[4]/td[4]').text
print('sn:'+sn)
time.sleep(15)


browser.quit()