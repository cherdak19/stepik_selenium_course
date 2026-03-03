from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


link = "https://SunInJuly.github.io/execute_script.html"
try:
   browser = webdriver.Chrome()
   browser.get(link)
   x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
   x = x_element.text
   y = str(math.log(abs(12*math.sin(int(x)))))
   input = browser.find_element(By.CSS_SELECTOR, "#answer")
   input.send_keys(y)

   button = browser.find_element(By.TAG_NAME, "button")
   checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
   radiobutt = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
   browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
   checkbox.click()
   radiobutt.click()
   button.click()
finally:
   time.sleep(30)
   browser.quit()