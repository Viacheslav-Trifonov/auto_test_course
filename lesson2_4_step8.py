import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

def main():
    try:
        WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), '$100')
        )
        button1 = browser.find_element(By.XPATH, "//button[@id='book']")
        button1.click()
        x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
        x = x_element.text
        x1 = calc(x)
        input1 = browser.find_element(By.XPATH, "//input[@id='answer']")
        input1.send_keys(x1)
        input2 = browser.find_element(By.XPATH, "//button[@id='solve']")
        input2.click()

    finally:
        time.sleep(10)
        browser.quit()

if __name__ == '__main__':
    main()
    