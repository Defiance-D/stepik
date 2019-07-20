from selenium import webdriver
from selenium.webdriver.common.by import By
import os 

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 1
file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла 

# Ссылки на первую и вторую версию формы регистрации
link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

# Код, который заполняет обязательные поля
textBox1 = browser.find_element(By.XPATH, "//input[@placeholder='Введите имя']")
textBox2 = browser.find_element(By.XPATH, "//input[@placeholder='Введите фамилию']")
textBox3 = browser.find_element(By.XPATH, "//input[@placeholder='Введите Email']")
textBox1.send_keys("test_string")
textBox2.send_keys("test_string")
textBox3.send_keys("test_string")

browser.find_element(By.ID, "file").send_keys(file_path)

button = browser.find_element_by_tag_name("button")
button.click()
