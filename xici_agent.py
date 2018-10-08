'''
elenium+chromedriver
'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
import requests
from bs4 import BeautifulSoup
import csv
#获得代理信息
def get_agents(n):
    all_agents=[]
    driver = webdriver.Chrome()
    url = 'http://www.xicidaili.com/nn/301'
    driver.get(url)
    for i in range(1, n+1):
        try:
            time.sleep(random.random() * 5)

            print ('打开第%d页' % i)

            text = driver.page_source

            soup = BeautifulSoup(text, 'html.parser')
            agents = soup.find_all(name='tr')
            for agent in agents:
                daili = agent.find_all(name='td')
                if daili:
                    ip = daili[1].text
                    port = daili[2].text
                    # ad = daili[3].text
                    nimi = daili[4].text
                    surv = daili[8].text
                    dail = {}
                    dail['IP'] = ip
                    dail['端口'] = port
                    dail['匿名度'] = nimi
                    # dail['地址'] = ad
                    dail['存活时间'] = surv
                    all_agents.append(dail)
            driver.find_element_by_class_name('next_page')
            driver.find_element_by_class_name('next_page').click()
        except:
            print('第%d页打开失败！！！'%i)
            continue

    return all_agents

#可用代理存入csv
def save_to_csv(goods):
    f = open('all_西刺代理_未验证.csv', 'a', newline='')
    headers = ['IP', '端口', '匿名度',  '存活时间']
    w = csv.DictWriter(f, fieldnames=headers)
    w.writeheader()
    for good in goods:
        w.writerow(good)

if __name__ == '__main__':
    n=int(input('查看几页代理：'))
    all_agents=get_agents(n)
    save_to_csv(all_agents)
    print('获得代理：%d'%len(all_agents))
