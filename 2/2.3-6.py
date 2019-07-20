from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

#browser.execute_script('document.getElementByClassName("trollface").classList.remove("trollface")')

button = browser.find_element_by_tag_name("button")
time.sleep(1)
button.click()

time.sleep(1)

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x_element = browser.find_element_by_id("input_value")
x = x_element.text
x = calc(x)

text = browser.find_element_by_id("answer")
text.send_keys(x)

button = browser.find_element_by_tag_name("button")
button.click()
