from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
textBox1=browser.find_element_by_class_name("first")
textBox2=browser.find_element_by_class_name("second")
textBox3=browser.find_element_by_class_name("third")
textBox1.send_keys("Хуй-Жопа")
textBox2.send_keys("Хуй-Жопа")
textBox3.send_keys("Хуй-Жопа")

# Отправляем заполненную форму
button = browser.find_element_by_tag_name("button")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
