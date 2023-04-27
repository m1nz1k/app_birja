from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from datetime import datetime

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw



# Создание объекта опций Chrome
chrome_options = Options()

# Включение headless-режима
chrome_options.add_argument('--headless')


driver = webdriver.Chrome(options=chrome_options)

# Список инструментов
instruments = [
    "Индекс РТС",
    "Индекс Мосбиржи",
    "Курс доллара к рублю",
    "Курс юаня к рублю",
    "Нефть марки Brent",
    "Курс золота",
    "Курс биткоина"
]

# Ссылки на страницы инструментов на Investing.com
urls = [
    "https://ru.investing.com/indices/rtsi",
    "https://ru.investing.com/indices/mcx",
    "https://ru.investing.com/currencies/usd-rub",
    "https://ru.investing.com/currencies/cny-rub",
    "https://ru.investing.com/commodities/brent-oil",
    "https://ru.investing.com/commodities/gold",
    "https://ru.investing.com/crypto/bitcoin/btc-usd"
]

count = 0
# Запрос данных для каждого инструмента
try:
    driver.maximize_window()
    for i in range(len(instruments)):
        count += 1
        now = datetime.now()
        date_time = now.strftime("%d.%m.%Y")
        url = urls[i]
        driver.get(url)
        time.sleep(1)
        price = driver.find_element(By.XPATH, "//span[@data-test='instrument-price-last']").text
        change_percent = driver.find_element(By.XPATH, "//span[@data-test='instrument-price-change-percent']").text
        message = f"{price} {change_percent}"
        if i == 0:
            rts = message
        elif i == 1:
            mosbir = message
        elif i == 2:
            usd_rub = message
        elif i == 3:
            cny_rub = message
        elif i == 4:
            brent = message
        elif i == 5:
            gold = message
        elif i == 6:
            btc = message
        print(f'Готово {count} из {len(instruments)}')



except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

# Открываем изображение
img = Image.open('image.jpg')

# Создаем объект ImageDraw для рисования на изображении
draw = ImageDraw.Draw(img)


font = ImageFont.truetype('Bungee.ttf', 70)
x = 700
y = 557

red = (255, 0, 0)
green = (0, 255, 0)

# Рисуем текст на изображении
if '+' in mosbir:
    draw.text((x, y), mosbir + '↑', font=font, fill=green)
else:
    draw.text((x, y), mosbir + '↓', font=font, fill=red)

font = ImageFont.truetype('Bungee.ttf', 60)
x = 2023
y = 501
if '+' in rts:
    draw.text((x, y), rts + '↑', font=font, fill=green)
else:
    draw.text((x, y), rts + '↓', font=font, fill=red)

font = ImageFont.truetype('Bungee.ttf', 60)
x = 290
y = 1125
if '+' in usd_rub:
    draw.text((x, y), usd_rub + '↑', font=font, fill=green)
else:
    draw.text((x, y), usd_rub + '↓', font=font, fill=red)

font = ImageFont.truetype('Bungee.ttf', 60)
x = 290
y = 1420
if '+' in cny_rub:
    draw.text((x, y), cny_rub + '↑', font=font, fill=green)
else:
    draw.text((x, y), cny_rub + '↓', font=font, fill=red)

font = ImageFont.truetype('Bungee.ttf', 60)
x = 290
y = 1675
if '+' in btc:
    draw.text((x, y), btc + '↑', font=font, fill=green)
else:
    draw.text((x, y), btc + '↓', font=font, fill=red)

font = ImageFont.truetype('Bungee.ttf', 60)
x = 1885
y = 1295
if '+' in brent:
    draw.text((x, y), brent + '↑', font=font, fill=green)
else:
    draw.text((x, y), brent + '↓', font=font, fill=red)

font = ImageFont.truetype('Bungee.ttf', 60)
x = 1735
y = 1717
if '+' in gold:
    draw.text((x, y), gold + '↑', font=font, fill=green)
else:
    draw.text((x, y), gold + '↓', font=font, fill=red)


# Сохраняем изображение в новый файл
img.save(f'image_{date_time}.jpg')
print('Скрипт завершен!')

