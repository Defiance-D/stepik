from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

#Идем по ссылке
link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

#Считываем формулу и считаем её
x_element = browser.find_element_by_id("treasure")
x = x_element.get_attribute("valuex")
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