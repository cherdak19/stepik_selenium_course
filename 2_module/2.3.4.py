from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


link = "http://suninjuly.github.io/alert_accept.html"
try:
   browser = webdriver.Chrome()
   browser.get(link)
   button = browser.find_element(By.TAG_NAME, "button")
   button.click()
   alert = browser.switch_to.alert
   alert.accept()
   x_element = browser.find_element(By.CSS_SELECTOR, "#input_value" )
   x = x_element.text
   input = browser.find_element(By.CSS_SELECTOR, "#answer" )  
   y = calc(int(x))
   input.send_keys(str(y))
   button2 = browser.find_element(By.CSS_SELECTOR, "[type ='submit']")
   button2.click()
finally:
   time.sleep(30)
   browser.quit()