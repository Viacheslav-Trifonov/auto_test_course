import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    input1 = browser.find_element(By.CSS_SELECTOR,
                                  "body > div > form > div.first_block > div.form-group.first_class > input")
    input1.send_keys("Ivan")
    time.sleep(1)
    input2 = browser.find_element(By.CSS_SELECTOR,
                                  "body > div > form > div.first_block > div.form-group.second_class > input")
    input2.send_keys("Petrov")
    time.sleep(1)
    input3 = browser.find_element(By.CSS_SELECTOR,
                                  "body > div > form > div.first_block > div.form-group.third_class > input")
    input3.send_keys("IvPert@mfs.com")
    time.sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.CSS_SELECTOR, "h1")

    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
