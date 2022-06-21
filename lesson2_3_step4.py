import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    option = browser.find_element(By.XPATH, "//button[@type='submit']")
    option.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = x_element.text
    x1 = calc(x)

    input1 = browser.find_element(By.XPATH, "//input[@id='answer']")
    input1.send_keys(x1)

    option3 = browser.find_element(By.XPATH, "//button[@type='submit']")
    option3.click()
finally:
    time.sleep(10)
    browser.quit()
