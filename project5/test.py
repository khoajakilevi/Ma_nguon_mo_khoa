from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains, ScrollOrigin
from time import sleep
import pandas as pd
import re
import sqlite3

# Kết nối cơ sở dữ liệu
ck = sqlite3.connect('ck1.db')
c = ck.cursor()
# Tạo bảng nếu chưa có
try:
    c.execute('''
        CREATE TABLE stock (
            id integer primary key autoincrement,
            day text,
            change text,
            closing_price integer,
            closing_price_DC integer,
            changed_volume integer,
            price integer,
            KLgTT integer, 
            GTTTin integer,
            open_price integer,
            highest_price integer,
            lowest_price integer,
            avg integer
        )
    ''')
except Exception as e:
    print(e)

# Hàm chèn dữ liệu vào cơ sở dữ liệu
def insert_data(day, change, closing_price, closing_price_DC, changed_volume, price, KLgTT, GTTTin, open_price, highest_price, lowest_price, avg):
    ck = sqlite3.connect('ck1.db')
    c = ck.cursor()
    c.execute('''
        INSERT INTO stock(day, change, closing_price, closing_price_DC, changed_volume, price, KLgTT, GTTTin, open_price, highest_price, lowest_price, avg)
        VALUES (:day, :change, :closing_price, :closing_price_DC, :changed_volume, :price, :KLgTT, :GTTTin, :open_price, :highest_price, :lowest_price, :avg)
    ''',
      {
          'day': day,
          'change': change,
          'closing_price': closing_price,
          'closing_price_DC': closing_price_DC,
          'changed_volume': changed_volume,  
          'price': price,
          'KLgTT': KLgTT,  
          'GTTTin': GTTTin,
          'open_price': open_price,
          'highest_price': highest_price,
          'lowest_price': lowest_price,
          'avg': avg
      })
    ck.commit()
    ck.close()

# Khởi tạo trình điều khiển
driver = webdriver.Chrome()
url = 'https://iboard.ssi.com.vn'
driver.get(url)   
sleep(3)

# Điều hướng đến trang cần thiết
name_xpath = '//*[@id="main-wrapper"]/div[1]/section[2]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]'
name_elm = driver.find_element(By.XPATH, value=name_xpath)
name_elm.click()
sleep(3)

tk_xpath = '//*[@id="stock-detail-tab"]/ul/li[7]/a'
tk_elm = driver.find_element(By.XPATH, value=tk_xpath)
tk_elm.click()
sleep(3)

# Thu thập dữ liệu từ các hàng
rows = driver.find_elements(By.CSS_SELECTOR, ".flex.p-2") 
for row in rows:
    
    columns = row.find_elements(By.TAG_NAME, "Div")
    day, change, closing_price, closing_price_DC, changed_volume, price, KLgTT, GTTTin, open_price, highest_price, lowest_price,avg =  (None,) * 12

    if len(columns) >= 11:
        day = columns[0].text
        change = columns[1].text.replace(",", "")
        closing_price = columns[2].text.replace(",", "")
        closing_price_DC = columns[3].text.replace(",", "")
        changed_volume = columns[4].text.replace(",", "")
        price = columns[5].text.replace(",", "")
        KLgTT = columns[6].text.replace(",", "")
        GTTTin = columns[7].text.replace(",", "")
        open_price = columns[8].text.replace(",", "")
        highest_price = columns[9].text.replace(",", "")
        lowest_price = columns[10].text.replace(",", "")
        avg = columns[11].text.replace(",", "")
    else:
        print(f"Không tìm thấy đủ cột.")

    insert_data(day, change, closing_price, closing_price_DC, changed_volume, price, KLgTT, GTTTin, open_price, highest_price, lowest_price, avg)

driver.quit()