from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = x_element.text
    y = calc(x)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    input1 = browser.find_element(By.XPATH, "//input[@id='answer']")
    input1.send_keys(y)

    option1 = browser.find_element(By.XPATH, "//input[@type='checkbox']")
    option1.click()

    option2 = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
    option2.click()

    option3 = browser.find_element(By.XPATH, "//button[@type='submit']")
    option3.click()

finally:
    time.sleep(10)
    browser.quit()
