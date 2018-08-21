import random
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
#获得代理信息
def get_agents(n):
    all_agents=[]
    driver = webdriver.Chrome()
    url = 'https://www.kuaidaili.com/free/inha/'
    driver.get(url)
    for i in range(1, n+1):
        try:
            driver.implicitly_wait(15)           # 隐性等待，最长等30秒
            time.sleep(random.random() * 3)
            print ('打开第%d页' % i)

            text = driver.page_source

            soup = BeautifulSoup(text, 'html.parser')
            tbody = soup.tbody
            trs = tbody.find_all(name='tr')
            for tr in trs:
                ip = tr.find(attrs={"data-title": "IP"}).text
                port = tr.find(attrs={"data-title": "PORT"}).text
                nimi = tr.find(attrs={"data-title": "匿名度"}).text
                #addres = tr.find(attrs={"data-title": "位置"}).text
                speed = tr.find(attrs={"data-title": "响应速度"}).text
                time = tr.find(attrs={"data-title": "最后验证时间"}).text
                dail = {}
                dail['IP'] = ip
                dail['端口'] = port
                dail['匿名度'] = nimi
                #dail['地址'] = addres
                dail['速度'] = speed
                dail['时间'] = time
                all_agents.append(dail)

            driver.find_element_by_class_name('next_page')
            driver.find_element_by_class_name('next_page').click()

        except:
            print('第%d页打开失败！！！'%i)
            continue
    return all_agents

#可用代理存入csv
def save_to_csv(goods):
    f = open('all_快代理_未验证.csv', 'a+', newline='')
    headers = ['IP', '端口', '匿名度', '存活时间']
    w = csv.DictWriter(f, fieldnames=headers)
    w.writeheader()
    for good in goods:
        w.writerow(good)

if __name__ == '__main__':
    n=int(input('查看几页代理：'))
    all_agents=get_agents(n)
    save_to_csv(all_agents)
    print('获得代理：%d'%len(all_agents))
