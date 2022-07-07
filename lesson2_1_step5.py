import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

def main():
    try:
        sunduk = browser.find_element(By.XPATH, "//img[@id='treasure']")
        x = sunduk.get_attribute('valuex')
        y = calc(x)
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

if __name__ == '__main__':
    main()
    