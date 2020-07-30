import datetime
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
starttime = datetime.datetime.now()
import execjs
# 这个是一个用来控制chrome以无界面模式打开的浏览器
# 创建一个参数对象，用来控制chrome以无界面的方式打开
chrome_options = Options()
# 后面的两个是固定写法 必须这么写
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--hide-scrollbars')
# 驱动路径 谷歌的驱动存放路径
path = r'C:\Users\mx-0123\AppData\Local\Google\Chrome\Application\chromedriver.exe'
# 创建浏览器对象
browser = webdriver.Chrome(executable_path=path, options=chrome_options)
url = 'https://10.0.10.223/login.html'
browser.get(url)
browser.implicitly_wait(10)
#time.sleep(2)
#browser.implicitly_wait(2)
browser.find_element_by_id('user').clear()
browser.find_element_by_id('user').send_keys('root')
# browser.find_element_by_name('password').clear()
browser.find_element_by_id('password').send_keys('moxiuroot')
browser.find_element_by_id('submit_lbl').click()
#time.sleep(10)
browser.switch_to.frame('treelist')
browser.execute_script("javascript:f_select('C33', '', '')")
browser.switch_to.default_content()
browser.switch_to.frame('da')
#time.sleep(6)
#browser.implicitly_wait(6)
t1 = browser.find_element_by_xpath\
    ('/html/body/div[4]/div[5]/div/div[4]/div/div/div/div/div/table/tbody/tr/td[12]/div[1]/span').text
t2 =browser.find_element_by_xpath\
            ('/html/body/div[4]/div[5]/div/div[4]/div/div/div/div/div/table/tbody/tr[2]/td[12]/div[1]/span').text

print('t1=', t1)
print('t2=', t2)
print(int(t1)+int(t2))
#time.sleep(2)
#browser.implicitly_wait(2)

# 切换到指定frame后执行注销功能
browser.switch_to.default_content()
browser.switch_to.frame('globalnav')
browser.execute_script('javascript:f_logout();')
browser.quit()
endtime = datetime.datetime.now()
print((endtime - starttime).seconds)