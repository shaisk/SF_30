import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from config import user_email, user_password


@pytest.fixture(autouse=True)
def browser():
    # Настройка Chrome WebDriver
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)

    # Переход на страницу входа
    driver.get('http://petfriends.skillfactory.ru/login')

    # Ввод email
    email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'email')))
    email_field.clear()
    email_field.send_keys(user_email)

    # Ввод пароля
    password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'pass')))
    password_field.clear()
    password_field.send_keys(user_password)

    # Нажатие кнопки входа
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
    login_button.click()

    # Переход на страницу "Мои питомцы"
    my_pets_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Мои питомцы")))
    my_pets_link.click()

    yield driver
    driver.quit()
