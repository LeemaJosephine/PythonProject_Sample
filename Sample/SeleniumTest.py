import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
        
def test_valid_headlessbrowsing():
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    #chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.guvi.in/")
    driver.maximize_window()
    driver.implicitly_wait(10)

    #Click Login button
    driver.find_element(By.XPATH, '(//button[@id="login-btn"])[1]').click()
    time.sleep(3)
    #Validate URL after clicking Login
    current_url = driver.current_url
    assert "https://www.guvi.in/sign-in/" in current_url

    #Validate Username field
    email=driver.find_element(By.XPATH,'//input[@id="email"]')
    assert email.is_displayed() and email.is_enabled()
    print("email:", email.is_enabled() and email.is_displayed())
    #Enter values in Username field
    email.send_keys("leema@hclguvi.com")
#
    #Validate Password field
    password=driver.find_element(By.XPATH,'//input[@id="password"]')
    assert password.is_displayed() and password.is_enabled()
    print("password:", password.is_enabled() and password.is_displayed())
    #Enter values in Password field
    password.send_keys("Naaskl@180399")

    #Validate Submit button
    submit_btn=driver.find_element(By.ID,'login-btn')
    driver.execute_script("arguments[0].scrollIntoView();", submit_btn)
    assert submit_btn.is_displayed() and submit_btn.is_enabled()
    print("submit_btn:", submit_btn.is_displayed() and submit_btn.is_enabled())
    #Click Submit button
    submit_btn.click()

    # driver.find_element(By.XPATH,'(//div[contains(@class,"account-box-toggler")])[1]').click()
    #
    # driver.find_element(By.XPATH,'(//p[text()="Sign Out"])[1]').click()

    profile = driver.find_element(By.XPATH, '(//div[contains(@class,"account-box-toggler")])[1]')
    driver.execute_script("arguments[0].click();", profile)

    logout = driver.find_element(By.XPATH, '(//p[text()="Sign Out"])[1]')
    driver.execute_script("arguments[0].click();", logout)
    time.sleep(30)


def test_invalid_headlessbrowsing():
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    #chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.guvi.in/")
    driver.maximize_window()
    driver.implicitly_wait(10)

    # Click Login button
    driver.find_element(By.XPATH, '(//button[@id="login-btn"])[1]').click()
    time.sleep(3)
    # Validate URL after clicking Login
    current_url = driver.current_url
    assert "https://www.guvi.in/sign-in/" in current_url

    # Validate Username field
    email = driver.find_element(By.XPATH, '//input[@id="email"]')
    assert email.is_displayed() and email.is_enabled()
    print("email:", email.is_enabled() and email.is_displayed())
    # Enter values in Username field
    email.send_keys("test@gmail.com")

    # Validate Password field
    password = driver.find_element(By.XPATH, '//input[@id="password"]')
    assert password.is_displayed() and password.is_enabled()
    print("password:", password.is_enabled() and password.is_displayed())
    # Enter values in Password field
    password.send_keys("")

    # Validate Submit button
    submit_btn = driver.find_element(By.ID, 'login-btn')
    assert submit_btn.is_displayed() and submit_btn.is_enabled()
    print("submit_btn:", submit_btn.is_displayed() and submit_btn.is_enabled())
    # Click Submit button
    submit_btn.click()
    time.sleep(3)
    error_msg = driver.find_element(By.XPATH,"(//div[@class='invalid-feedback'])[2]").text
    assert "Hey, Did you forgot your password? Try again." in error_msg

    time.sleep(45)
    #driver.quit()
