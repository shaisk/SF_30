import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_verify_homepage(browser):
    """Убедитесь, что пользователь находится на главной странице питомцев."""
    driver = browser
    assert driver.current_url == 'https://petfriends.skillfactory.ru/my_pets', "URL не соответствует ожидаемому"


def test_pets_have_required_fields(browser):
    """Проверяем, что у каждого питомца есть имя, возраст и порода."""
    driver = browser
    pet_rows = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

    for row in pet_rows:
        pet_info = row.text.split(' ')
        assert len(pet_info) == 3, f"У питомца отсутствуют необходимые данные: {row.text}"


def test_all_pets_present(browser):
    """Проверяем, что количество карточек питомцев соответствует статистике."""
    driver = browser
    statistics = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))

    total_pets = int(statistics.text.split('\n')[1].split(' ')[1])
    pet_cards = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

    assert total_pets == len(pet_cards), "Количество питомцев не соответствует статистике"
