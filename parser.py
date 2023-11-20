import codecs
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def main():
    driver.get('https://www.ozon.ru/')

    for i in range (1,100,25):
        driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight * {i}/100);")
        time.sleep(1)

    goods_arr = driver.find_elements(By.CLASS_NAME, "a5h cd5a dac5")
    goods_json=[]

    for good in goods_arr:
        desc = good.find_elements(By.CLASS.NAME, 'tsBody500Medium')[0].text
        price = good.find_elements(By.CLASS.NAME, 'c3118-a0')[0].text
        href = good.find_elements(By.CLASS.NAME, '_blank')[0].get.attribute('href')

        good_json = {

            'product':desc,
            'price':price,
            'link':href
        }
        goods_json.append((good_json))

        with codecs.open("vvv.json","WB", "utf=16"):
            json.dump(goods_json,stream,ensure_ascii=false)
main()