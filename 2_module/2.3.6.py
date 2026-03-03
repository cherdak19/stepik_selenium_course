from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


link = "https://suninjuly.github.io/redirect_accept.html"
try:
   browser = webdriver.Chrome()
   browser.get(link)
   button = browser.find_element(By.TAG_NAME, "button")
   button.click()
   new_window = browser.window_handles[1]
   browser.switch_to.window(new_window)
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