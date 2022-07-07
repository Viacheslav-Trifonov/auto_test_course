import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)

def main():
    try: 
        input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        input2.send_keys("Ivan")
        input3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        input3.send_keys("Ivan")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(10)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        time.sleep(10)
        browser.quit()

if __name__ == '__main__':
    main()
    