# Negative Scenario: Drag and Drop to an invalid target
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/droppable/")

wait = WebDriverWait(driver, 10)
# switch into the demo iframe (class name used on the page)
wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, ".demo-frame")))

source = wait.until(EC.presence_of_element_located((By.ID, "draggable")))
target = wait.until(EC.presence_of_element_located((By.ID, "droppable")))

ActionChains(driver).drag_and_drop(source, target).perform()

# optional: switch back to main document
driver.switch_to.default_content()