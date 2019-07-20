from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
browser = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"
browser.get(link)

x_element = browser.find_element_by_id("input_value")
x = x_element.text
x = calc(x)

#Ищем куда вводить результат и вводим его
text = browser.find_element_by_id("answer")
text.send_keys(x)

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

#Тыкаем чек-бокс "Подтверждаю, что являюсь роботом"
check=browser.find_element_by_id("robotCheckbox")
check.click()

#Тыкаем  на "Роботы рулят"
radio = browser.find_element_by_id("robotsRule")
radio.click()

button.click()
assert True