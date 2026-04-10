import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_facebook_signup(driver):
    driver.get("https://www.facebook.com/")

    # Click Create New Account
    driver.find_element(By.XPATH, "//a[text()='Create new account']").click()
    time.sleep(3)

    # Fill form
    driver.find_element(By.NAME, "firstname").send_keys("Leema")
    driver.find_element(By.NAME, "lastname").send_keys("Josephine")

    driver.find_element(By.NAME, "reg_email__").send_keys("test123@gmail.com")
    driver.find_element(By.NAME, "reg_passwd__").send_keys("Test@1234")

    # Select DOB
    Select(driver.find_element(By.ID, "day")).select_by_value("10")
    Select(driver.find_element(By.ID, "month")).select_by_value("5")
    Select(driver.find_element(By.ID, "year")).select_by_value("1998")

    # Select Gender
    driver.find_element(By.XPATH, "//input[@value='1']").click()

    # Click Sign Up
    driver.find_element(By.NAME, "websubmit").click()

    time.sleep(5)