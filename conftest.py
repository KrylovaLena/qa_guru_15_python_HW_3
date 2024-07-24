import pytest
from selene import browser


@pytest.fixture(scope="function")
def browser_setup():
    # Открыть браузер на нужной странице
    browser.config.browser_name = 'chrome'
    # Установить размер окна браузера
    browser.config.window_width = 520
    browser.config.window_height = 470
    # Открыть выбранную страницу Google
    browser.open('https://google.com')
    yield
    browser.quit()



