import datetime
import execjs
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
starttime = datetime.datetime.now()
# 这个是一个用来控制chrome以无界面模式打开的浏览器
# 创建一个参数对象，用来控制chrome以无界面的方式打开
chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--ignore-certificate-errors')
# 驱动路径 谷歌的驱动存放路径
path = r'C:\Users\mx-0123\AppData\Local\Google\Chrome\Application\chromedriver.exe'
# 创建浏览器对象
browser = webdriver.Chrome(executable_path=path, options=chrome_options)
# 通过读取文件获取需要连接的远控卡信息
ms =open(r'C:\Users\mx-0123\Desktop\ip.txt', 'r')
browser.implicitly_wait(10)
for nu in ms.readlines():
    with open(r'C:\Users\mx-0123\Desktop\check_result.txt', 'a') as mon:
        url = 'https://'+str(nu)+'/login.html'
        browser.get(url)
        print('url:', url)
        browser.find_element_by_id('user').send_keys('root')
        browser.find_element_by_id('password').send_keys('moxiuroot')
        browser.find_element_by_id('submit_lbl').click()
        browser.switch_to.frame('treelist')
        browser.execute_script("javascript:f_select('C33', '', '')")
        browser.switch_to.default_content()
        browser.switch_to.frame('da')
        # 获取第一个raid 信息
        raid1 = browser.find_element_by_xpath\
            ('/html/body/div[4]/div[5]/div/div[4]/div/div/div/div/div/table/tbody/tr[1]/td[4]/span').text
        if (raid1 == '降级'):
            result = (nu + 'raid 1 error' + '\n')
            mon.write(result)
        else:
            result = (nu + 'raid 1 success' + '\n')
            mon.write(result)

        # 获取第二个raid 信息
        try:
            raid2 = browser.find_element_by_xpath \
            ('/html/body/div[4]/div[5]/div/div[4]/div/div/div/div/div/table/tbody/tr[2]/td[4]/span').text
            print('raid2 exsit')
            if (raid2 == '降级'):
                result = (nu + 'raid 2 error' + '\n')
                mon.write(result)
            else:
                 result = (nu + 'raid 2 success' + '\n')
                 mon.write(result)
        except:
            print('raid2 not  exsit')
        # 切换到指定frame后执行注销功能
        mon.write('===================\n')
        browser.switch_to.default_content()
        browser.switch_to.frame('globalnav')
        browser.execute_script('javascript:f_logout();')
browser.quit()
endtime = datetime.datetime.now()
print((endtime - starttime).seconds)