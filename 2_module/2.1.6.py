from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
   return str(math.log(abs(12 * math.sin(int(x)))))

link = "https://suninjuly.github.io/get_attribute.html"

try:
   browser = webdriver.Chrome()
   browser.get(link)

   x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
   x = x_element.get_attribute("valuex")
   print("икс равно", x)
   source = x_element.get_attribute("src")
   print ("сорс равно", source)
   
   # y = calc(x)
   # answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
   # answer_input.send_keys(y)

   # option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
   # option1.click()
   # option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
   # option2.click()
   # button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
   # button.click()


finally:
   time.sleep(30)
   browser.quit()