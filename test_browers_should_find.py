from selene import browser, be, have


def test_google_search():
    browser.open('')
    # Вводим поисковый запрос и проверяем, результаты поиска соответствуют ожидаемым
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_no_expected_results():
    browser.open('')
    # Вводим случайный набор символов, по которому не ожидаем результатов поиска
    browser.element('[name="q"]').should(be.blank).type('jmhgnfdfdghfjhfmjh4r').press_enter()
    browser.element('[id="botstuff"]').should(have.text('По запросу jmhgnfdfdghfjhfmjh4r ничего не найдено.'))

