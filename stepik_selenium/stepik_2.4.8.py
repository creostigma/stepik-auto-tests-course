from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button1 = browser.find_element_by_id("book")
    button1.click()

    x = browser.find_element_by_id("input_value").text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_value = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(x_value)

    button2 = browser.find_element_by_id("solve")
    button2.click()

finally:
    time.sleep(7)
    browser.quit()