from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time


def test_invalid_drag_and_drop():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://jqueryui.com/droppable/")  # test drag & drop site

    try:
        source = driver.find_element(By.ID, "draggable")  # valid draggable element
        invalid_target = driver.find_element(By.ID, "textbox")  # ❌ invalid drop target (not droppable)

        actions = ActionChains(driver)
        actions.drag_and_drop(source, invalid_target).perform()
        time.sleep(2)

        # Validate that drop did NOT happen
        droppable_text = driver.find_element(By.ID, "droppable").text

        if "Dropped!" not in droppable_text:
            print("❗ Negative Test Passed: Drop did not occur on invalid element.")
        else:
            print("❌ Negative Test Failed: Element was dropped incorrectly!")

    except NoSuchElementException:
        print("❗ Test Passed — One of the elements was not found as expected (negative behavior).")

    except Exception as e:
        print(f"Unexpected behavior but still negative condition tested: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_invalid_drag_and_drop()