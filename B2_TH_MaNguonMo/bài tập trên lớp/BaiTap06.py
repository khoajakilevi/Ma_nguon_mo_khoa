from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import re

#tao dataframe rong va noi chua link
all_links =[] 
d =pd.DataFrame({'name': [], 'birth': [], 'death': [], 'nationality': []})


#lay tat ca duong dan de truy cap den painter
for i in range(65, 91):
    driver = webdriver.Chrome()
    url = "https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22"+chr(i)+"%22"
    #mo trang web
    driver.get(url)
    try:
        #doi khoang chung 2s
        time.sleep(3)

        #lay ra tat ca the ul
        ul_tags = driver.find_elements(By.TAG_NAME, "ul")

        #chon ul thu 21
        ul_painters = ul_tags[20]

        #lay tat ca the <li> thuoc ul_painters
        li_tags = ul_painters.find_elements(By.TAG_NAME, "li")
        # #tao danh sach cac url
        links = [tag.find_element(By.TAG_NAME,"a").get_attribute("href") for tag in li_tags]
        for x in links:
            all_links.append(x)
        #tao danh sach cac title
        # titles = [tag.find_element(By.TAG_NAME,"a").get_attribute("title") for tag in li_tags]

        # #in ra danh sach
        # for link in links:
        #     print(link)

        #in ra danh sach
        # for title in titles:
        #     print(title)
   
    except:
        print("Error!!")
    #tat man hinh
    driver.quit()

############################################################
for link in all_links:
    try:
        #khoi tao webdriver
        driver = webdriver.Chrome()

        #mo trang
        url = "https://en.wikipedia.org/wiki/Edvard_Munch"
        driver.get(url)

        #doi 2s
        time.sleep(2)

        #lay ten hoa si
        try:
            name = driver.find_element(By.TAG_NAME, "h1").text
        except:
            name = ""


        #lay ngay sinh hoa si
        try:
            birth_element = driver.find_element(By.XPATH, "//th[text()='Born']/following-sibling::td")
            birth = birth_element.text
            birth = re.findall(r'[0-9]{1,2}+\s+[A-Za-z]+\s+[0-9]{4}', birth)[0]
        except:
            birth = ""

        #lay ngay mat hoa si
        try:
            death_element = driver.find_element(By.XPATH, "//th[text()='Died']/following-sibling::td")
            death = death_element.text
            death = re.findall(r'[0-9]{1,2}+\s+[A-Za-z]+\s+[0-9]{4}', death)[0]
        except:
            death = ""

        #lay quoc tich hoa si
        try:
            nationality_element = driver.find_element(By.XPATH, "//th[text()='Nationality']/following-sibling::td")
            nationality = nationality_element.text
        except:
            nationality = ""

        #tao dictionary thong tin hoa si
        painter = {'name': name, 'birth': birth, 'death': death, 'nationality': nationality}
        painter_df = pd.DataFrame([painter])
    except:
        print("Error!!!!!!!!!!!!!!!")

#th
d = pd.concat([d, painter_df], ignore_index=True)

print(d)

driver.quit()