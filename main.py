import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from datetime import datetime

s = Service(executable_path=r'C:\Users\Евгений\PycharmProjects\app_birja\chromedriver\chromedriver.exe')
driver = webdriver.Chrome(service=s)

# Список инструментов
instruments = [
    "Индекс РТС",
    "Индекс Мосбиржи",
    "Курс доллара к рублю",
    "Курс юаня к рублю",
    "Нефть марки Brent",
    "Индекс DOW JONES",
    "Курс золота",
    "Фьючерс на газ"
]

# Ссылки на страницы инструментов на Investing.com
urls = [
    "https://ru.investing.com/indices/rtsi",
    "https://ru.investing.com/indices/mcx",
    "https://ru.investing.com/currencies/usd-rub",
    "https://ru.investing.com/currencies/cny-rub",
    "https://ru.investing.com/commodities/brent-oil",
    "https://ru.investing.com/indices/us-30",
    "https://ru.investing.com/commodities/gold",
    "https://ru.investing.com/crypto/bitcoin/btc-rub"
]


# Запрос данных для каждого инструмента
try:
    driver.maximize_window()
    for i in range(len(instruments)):
        now = datetime.now()
        date_time = now.strftime("%d.%m.%Y")
        url = urls[i]
        driver.get(url)
        time.sleep(2)
        price = driver.find_element(By.XPATH, "//span[@data-test='instrument-price-last']").text
        change_percent = driver.find_element(By.XPATH, "//span[@data-test='instrument-price-change-percent']").text
        message = f"{date_time} {instruments[i]}: {price} {change_percent}"
        print(message)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

