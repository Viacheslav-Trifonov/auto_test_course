import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/cats.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    option = browser.find_element(By.ID, "button")
finally:
    time.sleep(10)
    browser.quit()
