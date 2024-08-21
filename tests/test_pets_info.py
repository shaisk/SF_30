import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_unique_pet_names(browser):
    """Проверяем, что все питомцы имеют уникальные имена."""
    driver = browser
    pet_rows = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

    pet_names = [row.text.split(' ')[0] for row in pet_rows]

    assert len(pet_names) == len(set(pet_names)), "Есть повторяющиеся имена питомцев"


def test_no_duplicate_pets(browser):
    """Убеждаемся, что нет повторяющихся карточек питомцев."""
    driver = browser
    pet_rows = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

    pets_data = [row.text.replace('\n', '').replace('×', '') for row in pet_rows]

    assert len(pets_data) == len(set(pets_data)), "Найдены дублирующиеся карточки питомцев"


def test_pets_with_photos(browser):
    """Проверяем, что у как минимум половины питомцев есть фото."""
    driver = browser
    statistics = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))
    images = driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')

    total_pets = int(statistics.text.split('\n')[1].split(' ')[1])
    pets_with_photos = sum(1 for img in images if img.get_attribute('src'))

    assert pets_with_photos >= total_pets // 2, "У менее половины питомцев есть фото"
