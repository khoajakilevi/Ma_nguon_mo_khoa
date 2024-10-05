from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#khoi tao webdriver
driver = webdriver.Chrome()

#mo trang web
url = "https://en.wikipedia.org/wiki/List_of_painters_by_name"
# url = "https://truyenqqto.com/"
driver.get(url)

#doi khoang chung 2s
time.sleep(2)

#lay tat ca cac the <a>
tags = driver.find_elements(By.TAG_NAME, "a")

#tao danh sach lien ket
links = [tag.get_attribute("href") for tag in tags]

#in ra man hinh
for link in links:
    print(link)

driver.quit()