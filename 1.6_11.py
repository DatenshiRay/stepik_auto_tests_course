from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    url = "https://suninjuly.github.io/registration1.html"
    driver = webdriver.Chrome()
    driver.get(url)

    # Заполнение обязательных полей формы
    first_name = driver.find_element(By.CSS_SELECTOR, '.first_block .first')
    first_name.send_keys('Misha')
    
    last_name = driver.find_element(By.CSS_SELECTOR, '.first_block .second')
    last_name.send_keys('Mishka')
    
    email_field = driver.find_element(By.CSS_SELECTOR, '.first_block .third')
    email_field.send_keys('mishka@mail.com')

    # Нажимаем на кнопку отправки формы
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    # Ожидание загрузки страницы с результатами
    time.sleep(1)

    # Извлечение текста приветствия
    greeting_element = driver.find_element(By.TAG_NAME, "h1")
    greeting_message = greeting_element.text

    # Проверка, что текст соответствует ожидаемому
    assert "Congratulations! You have successfully registered!" == greeting_message

finally:
    # Пауза перед закрытием браузера для просмотра
    time.sleep(10)
    # Завершаем работу браузера
    driver.quit()