from selenium import webdriver

driver = webdriver.Chrome()

# 打开ip138网站
driver.get("http://www.ip138.com/")

# 定位到内嵌网页(iframe),并进入表单
####xf = driver.find_element_by_xpath('/html/body/p[1]/a')
driver.switch_to.frame(0)
#driver.switch_to.frame(name or id) #默认直接取表单的id 或name属性,如果都没有则通过上边的定位方式
print(driver.find_element_by_xpath('html/body/p[1]/a').text)

# 退出内嵌网页(iframe)，如果想操作外层的页面，不退出是会报错的
driver.switch_to.default_content()
####print(driver.find_element_by_xpath('/html/body/div/div[3]/h3').text)

driver.quit()