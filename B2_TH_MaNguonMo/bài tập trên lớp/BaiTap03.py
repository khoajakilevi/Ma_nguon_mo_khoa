from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#khoi tao webdriver
driver = webdriver.Chrome()

#mo trang web
url = "https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22U%22"
driver.get(url)

#doi khoang chung 2s
time.sleep(2)

#lay ra tat ca the ul
ul_tags = driver.find_elements(By.TAG_NAME, "ul")

#chon ul thu 21
ul_painters = ul_tags[20]

#lay tat ca thuoc ul_painters
li_tags = ul_painters.find_elements(By.TAG_NAME, "li")
#tao danh sach cac url
links = [tag.find_element(By.TAG_NAME,"a").get_attribute("href") for tag in li_tags]

#tao danh sach cac title
titles = [tag.find_element(By.TAG_NAME,"a").get_attribute("title") for tag in li_tags]

#in ra danh sach
for link in links:
    print(link)

#in ra danh sach
print("-------------------------------------------------------")
for title in titles:
    print(title)

#tat man hinh
driver.quit()