import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_xpath_form"

browser = webdriver.Chrome()
browser.get(link)

def main():
    try:
        input1 = browser.find_element(By.NAME, 'first_name')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.NAME, 'last_name')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, 'city')
        input3.send_keys("Smolensk")
        input4 = browser.find_element(By.ID, "country")
        input4.send_keys("Russia")
        button = browser.find_element(By.XPATH, "//button[@type='submit']")
        button.click()

    finally:
        time.sleep(30)
        browser.quit()


if __name__ == '__main__':
    main()
