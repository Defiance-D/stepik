from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

#Идем по ссылке
link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

#Считываем формулу и считаем её
x_element = browser.find_element_by_id("input_value")
x = x_element.text
x = calc(x)

#Ищем куда вводить результат и вводим его
text = browser.find_element_by_id("answer")
text.send_keys(x)

#Тыкаем чек-бокс "Подтверждаю, что являюсь роботом"
check=browser.find_element_by_id("robotCheckbox")
check.click()

#Тыкаем  на "Роботы рулят"
radio = browser.find_element_by_id("robotsRule")
radio.click()

# Ищем кнопку и тыкаем её
button = browser.find_element_by_xpath("//button[@type='submit']")
button.click()