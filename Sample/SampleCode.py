#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.service import Service
#
#
#
# driver = webdriver.Chrome()
# driver.get('https://www.guvi.in/courses/?current_tab=paidcourse')
# labels = driver.find_elements(By.XPATH,"//ul//child::div/input[@type='checkbox'][1]")
# for label in labels:
#     print(label.text)
#
# print(driver.title)
#

import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")
time.sleep(5)

search = driver.find_element(By.ID,"APjFqb")
search.send_keys("Selenium")
search.send_keys(Keys.RETURN)