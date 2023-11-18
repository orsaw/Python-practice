import codecs
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json

            #Не поняла как установить pip install selenium сработал а потом выдаёт ошибку ModuleNotFoundError: No module named 'selenium'
            #можете кинуть все библиотеки которые надо скачать пожалуйста, спасибо!!!!!!!!

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def main():
    driver.get("https://www.wildberries.ru/")

    for i in range(1, 100, 15):
        driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight * {i} / 100);")
        time.sleep(1)

    goods_arr = driver.find_elements(By.CLASS_NAME, "product-cardwrapper")
    goods_json = []

    for good in goods_arr:
        description = good.find_elements(By.CLASS_NAME, 'product-cardname')[0].text
        price = good.find_elements(By.CLASS_NAME, 'pricelower-price')[0].text
        href = good.find_elements(By.CLASS_NAME, 'product-cardlink')[0].get_attribute('href')

        good_json = {
            'product': description,
            'price': price,
            'link': href
        }
        goods_json.append(good_json)

    with codecs.open("vvv.json", "wb", "utf=16") as stream:
        json.dump(goods_json, stream, ensure_ascii=False)


main()
