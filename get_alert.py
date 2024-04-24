from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    num = browser.find_element(By.ID, "input_value")
    x = int(num.text)
    y = math.log(abs(12 * math.sin((x))))
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    button2 = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button2.click()


finally:
    time.sleep(5)
    browser.quit()
