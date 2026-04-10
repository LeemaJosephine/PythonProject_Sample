import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--lang=en-US")

driver = webdriver.Chrome(options=options)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[text()=' Login ']").click()



time.sleep(20)