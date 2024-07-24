from selene import browser, be, have


def test_google_search(browser_setup):
    # Вводим поисковый запрос и проверяем, результаты поиска соответствуют ожидаемым
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_no_expected_results(browser_setup):
    # Вводим случайный набор символов, по которому не ожидаем результатов поиска
    browser.element('[name="q"]').should(be.blank).type('fghjkhgfEFGhjnbvc456Fgn').press_enter()
    browser.element('[id="botstuff"]').should(have.text('По запросу fghjkhgfEFGhjnbvc456Fgn ничего не найдено.'))

