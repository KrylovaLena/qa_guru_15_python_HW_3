import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def browser_setup():
    # Установить размер окна браузера
    browser.config.window_width = 1280
    browser.config.window_height = 1024
    # Установить base_url -  страницу Google
    browser.config.base_url = 'https://google.com'
    yield
    browser.quit()



