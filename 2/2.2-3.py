from selenium import webdriver
from selenium.webdriver.support.ui import Select

#Идем по ссылке
#link = "http://suninjuly.github.io/selects1.html"
link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

#Считываем формулу и считаем её
x = browser.find_element_by_id("num1").text
y = browser.find_element_by_id("num2").text
z = int(x) + int(y)

Select(browser.find_element_by_tag_name("select")).select_by_value(str(z))

# Ищем кнопку и тыкаем её
button = browser.find_element_by_xpath("//button[@type='submit']")
button.click()
