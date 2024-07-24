import pytest
from selene import browser

@pytest.fixture(scope="function", autouse=True)
def browser_setup():
    # Установить размер окна браузера
    browser.config.window_width = 1280
    browser.config.window_height = 1024

    # Закрыть браузер после выполнения теста
    yield
    browser.quit()