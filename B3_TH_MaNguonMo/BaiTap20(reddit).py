from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
import time
import pandas as pd
import getpass

# Đường dẫn đến file thực thi geckodriver
gecko_path = r"C:/Users/Admin/OneDrive/Máy tính/python/geckodriver.exe"

# Khởi tởi đối tượng dịch vụ với đường geckodriver
ser = Service(gecko_path)

# Tạo tùy chọn
options = webdriver.chrome.options.Options()
options.binary_location ="c:\Program Files\Google\Chrome\Application\chrome.exe"
# Thiết lập firefox(chrome) chỉ hiện thị giao diện
options.headless = False

# Khởi tạo driver
driver = webdriver.Chrome()

# Tạo url
url = 'https://www.reddit.com/login/'

# Truy cập
driver.get(url)

# # Tạm dừng khoảng 2 giây
# time.sleep(1)

# #nhập thông tin người dùng
my_email = input('Please provide your email: ')
my_password = getpass.getpass('Please provide your password: ')

# #đăng nhập
# username_input = driver.find_element(By.XPATH, "//input[@id='login-username']")
# password_input = driver.find_element(By.XPATH, "//input[@id='login-password']")

# #nhập thông tin và nhấp nut enter
# username_input.send_keys(my_email)
# password_input.send_keys(my_password + Keys.ENTER)
# time.sleep(15)

actionChains = ActionChains(driver)
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
time.sleep(1)
actionChains.send_keys(my_email).perform()
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
actionChains.send_keys(my_password+Keys.ENTER).perform()
time.sleep(10)

#truy cap trang post bai
url2 = "https://www.reddit.com/submit?type=TEXT"
driver.get(url2)
time.sleep(2)

for i in range(14):
    actionChains.key_down(Keys.TAB).perform()
    time.sleep(1)
    
actionChains.send_keys('Vi du post').perform()

actionChains.key_down(Keys.TAB).perform()
actionChains.send_keys('Truong Minh Khoa').perform()

for i in range(2):
    actionChains.key_down(Keys.TAB).perform()
    time.sleep(2)

actionChains.key_down(Keys.Enter).perform()


time.sleep(15)
driver.quit()