import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

def main():
    try:
        input1 = browser.find_element(By.XPATH, "//input[@name='firstname']")
        input1.send_keys('Vladimir')
        input2 = browser.find_element(By.XPATH, "//input[@name='lastname']")
        input2.send_keys('Ivanov')
        input3 = browser.find_element(By.XPATH, "//input[@name='email']")
        input3.send_keys('www@ya.ru')
        element = browser.find_element(By.XPATH, "//input[@name='file']")
        current_dir = os.path.abspath(os.path.dirname(__file__))    
        file_path = os.path.join(current_dir, 'txt.txt')           
        element.send_keys(file_path)
        option3 = browser.find_element(By.XPATH, "//button[@type='submit']")
        option3.click()

    finally:
        time.sleep(10)
        browser.quit()

if __name__ == '__main__':
    main()
    