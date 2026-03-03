from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"

try:
   browser = webdriver.Chrome()
   browser.get(link)

   x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
   y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
   x = x_element.text
   y = y_element.text
   u = int(x) + int(y)
   select = Select(browser.find_element(By.TAG_NAME, "select"))
   select.select_by_value(str(u))

   browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()


finally:
   time.sleep(30)
   browser.quit()