from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import math
import time


link = "https://suninjuly.github.io/file_input.html"
try:
   browser = webdriver.Chrome()
   browser.get(link)
   input_name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
   input_name.send_keys("Ыыы")
   input_2nd_name = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
   input_2nd_name.send_keys("Ыыы2")
   input_email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
   input_email.send_keys("em@il.ru")
   input_file = browser.find_element(By.CSS_SELECTOR, "#file")
   current_dir = os.path.abspath(os.path.dirname('2.2.8.py'))
   file_path = os.path.join(current_dir, '1.2.5.txt')
   input_file.send_keys(file_path)
   button = browser.find_element(By.TAG_NAME, "button")
   button.click()
finally:
   time.sleep(30)
   browser.quit()