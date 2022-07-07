import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

def main():
    try:
        x1_element = browser.find_element(By.XPATH, "//span[@id='num1']")
        x1 = int(x1_element.text)
        x2_element = browser.find_element(By.XPATH, "//span[@id='num2']")
        x2 = int(x2_element.text)
        y = x1 + x2
        select = Select(browser.find_element(By.XPATH, "//select[@id='dropdown']"))
        select.select_by_value(str(y))
        option3 = browser.find_element(By.XPATH, "//button[@type='submit']")
        option3.click()

    finally:
        time.sleep(10)
        browser.quit()

if __name__ == '__main__':
    main()
    