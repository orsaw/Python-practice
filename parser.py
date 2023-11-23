
from selenium.webdriver.common.by import By
import time
import seleniumbase as sb
from selenium_stealth import stealth
import json


driver = sb.Driver(browser="Chrome", headless=False, uc=True)
stealth(driver,
        languages=["ru-RU", "ru"],ru
        vendor="Google Inc.",
        platform="Win64",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

def main():
    driver.get("https://www.ozon.ru")

    for i in range(1, 100, 15):
        driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight * {i} / 100);")
        time.sleep(1)

    goods_arr = driver.find_elements(By.CLASS_NAME, "ah5")
    print(len(goods_arr))
    goods_json = []

    for good in goods_arr:
        price = good.find_elements(By.CLASS_NAME, 'c3118-a0')[0].text
        price = str(price.encode('unicode_escape'))[2:-1].replace("\\u2009", '').replace("\\u20bd", "").replace("\\u2212", "").replace("\\", "").split("n")
        if int(price[0]) < 200:
            continue
        price = " ".join(price)
        description = good.find_elements(By.CLASS_NAME, "b7a.ab9.ba9.h6a")[0].text
        href = good.find_elements(By.CLASS_NAME, 'a5g.ah6')[0].get_attribute('href')

        good_json = {
            'product': description,
            'price': price,
            'link': href
        }
        goods_json.append(good_json)

    with open("out.json", "w+", encoding="UTF-8") as json_file:
        json.dump(goods_json, json_file, ensure_ascii=False, indent=4)

    main()