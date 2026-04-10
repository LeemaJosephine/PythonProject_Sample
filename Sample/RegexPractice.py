from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ---------- Test Data ----------
USERNAME = "leematestuser"
PASSWORD = "leematestuser"

# ---------- Initialize WebDriver ----------
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.demoblaze.com")

wait = WebDriverWait(driver, 10)

try:
    # Click on "Log in" link
    login_link = wait.until(EC.element_to_be_clickable((By.ID, "login2")))
    login_link.click()

    # Wait for login modal
    username_input = wait.until(EC.visibility_of_element_located((By.ID, "loginusername")))
    password_input = driver.find_element(By.ID, "loginpassword")

    # Enter credentials
    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)

    # Click login button
    login_button = driver.find_element(By.XPATH, "//button[text()='Log in']")
    login_button.click()

    # Wait for successful login (username appears)
    wait.until(EC.visibility_of_element_located((By.ID, "nameofuser")))

    print("✅ Login Successful!")

except Exception as e:
    print("❌ Login Failed:", e)

finally:
    time.sleep(3)
    driver.quit()