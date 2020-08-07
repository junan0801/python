import datetime
import execjs
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
starttime = datetime.datetime.now()
# 这个是一个用来控制chrome以无界面模式打开的浏览器
# 创建一个参数对象，用来控制chrome以无界面的方式打开
chrome_options = Options()
#chrome_options.add_argument('--headless')
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
        # 判断机器是否为 idrac 7,如果不为7 版本直接退出并关闭浏览器
        try:
            browser.find_element_by_id('servertype')
        except:
            print('旧版本远控卡,无法查看磁盘,无需登录该机器')
            mon.write(nu + 'is idrac 6  exsit \n============\n')
            continue
        browser.find_element_by_id('user').send_keys('root')
        browser.find_element_by_id('password').send_keys('moxiuroot')
        browser.find_element_by_id('submit_lbl').click()
        try:
            browser.find_element_by_name('treelist')
        except:
            print('无treelist')
            mon.write(nu + 'treelist not   exsit \n============\n')
            continue
            #time.sleep(20)
            #print(nu+'will sleep')
        browser.switch_to.frame('treelist')
        browser.execute_script("javascript:f_select('C33', '', '')")
        browser.switch_to.default_content()
        browser.switch_to.frame('da')
        try:
            raid1 = browser.find_element_by_xpath \
                ('/html/body/div[4]/div[5]/div/div[4]/div/div/div/div/div/table/tbody/tr[1]/td[4]/span').text
            print('raid1 exsit')
            if (raid1 == '降级'):
                result = (nu + 'raid 1 error' + '\n')
                mon.write(result)
            else:
                result = (nu + 'raid 1 success' + '\n')
                mon.write(result)
        except:
            print('raid1 not  exsit')
            mon.write(nu + 'raid 2 not exsit')
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
            mon.write(nu + 'raid 2 not exsit')
        # 切换到指定frame后执行注销功能
        mon.write('\n===================\n')
        browser.switch_to.default_content()
        browser.switch_to.frame('globalnav')
        browser.execute_script('javascript:f_logout();')
browser.quit()
endtime = datetime.datetime.now()
print((endtime - starttime).seconds)