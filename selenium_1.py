from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()

url='https://www.baidu.com/'

driver.get(url)

text=driver.find_element_by_id('wrapper').text

print(text)
print(driver.title)

#页面截屏保存为index.png
driver.save_screenshot('index.png')

#找到输入框id为kw，写入'大熊猫'
driver.find_element_by_id('kw').send_keys(u'大熊猫')

#找到搜索按钮id为su，并点击
driver.find_element_by_id('su').click()

#若不延时，截屏时网页可能还未完全加载完。。。
time.sleep(2)

driver.save_screenshot('大熊猫.png')

print(driver.get_cookies())

#模仿ctrl+a全选
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')

#driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')     #模仿ctrl+x剪切
driver.find_element_by_id('kw').clear()                          #clear()清除

driver.find_element_by_id('kw').send_keys(u'书包')

#driver.find_element_by_id('su').click()
driver.find_element_by_id('su').send_keys(Keys.RETURN)            #模仿回车键

time.sleep(4)

driver.save_screenshot('书包.png')

driver.quit()