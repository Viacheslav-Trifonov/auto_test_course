import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

def main():
    try:
        browser.get("http://suninjuly.github.io/huge_form.html")
        elements = browser.find_elements(By.TAG_NAME, 'input')
        for element in elements:
            element.send_keys("Мой ответ")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

    finally:
        time.sleep(30)
        browser.quit()


if __name__ == '__main__':
    main()      
