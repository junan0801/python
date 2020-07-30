import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 这个是一个用来控制chrome以无界面模式打开的浏览器
# 创建一个参数对象，用来控制chrome以无界面的方式打开
chrome_options = Options()
# 后面的两个是固定写法 必须这么写
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--windows-size=1920*1080')
chrome_options.add_argument('--hide-scrollbars')
# 驱动路径 谷歌的驱动存放路径
path = r'C:\Users\mx-0123\AppData\Local\Google\Chrome\Application\chromedriver.exe'
# 创建浏览器对象
browser = webdriver.Chrome(executable_path=path, options=chrome_options)
url = 'https://cn.bing.com/'
browser.get(url)
browser.find_element_by_id('sb_form_q').clear()
browser.find_element_by_id('sb_form_q').send_keys('python 3')
browser.find_element_by_id('sb_form_go').click()
text1 = browser.find_element_by_link_text('').text()
print(text1)

time.sleep(50)


browser.quit()
