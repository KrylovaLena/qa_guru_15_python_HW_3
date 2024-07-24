# qa_guru_15_python_HW_3
Выполнение домашнего задания №3

Установка зависимостей

$ pip install -r requirements.txt

Запуск автотестов 

$ pytest .

1. В conftest.py хранится fixture для установки конфигурации браузера и открытия страницы (browser_setup)
2. В test_browers_should_find.py тесты:

- test_google_search - Вводим поисковый запрос и проверяем, результаты поиска соответствуют ожидаемым
- test_search_no_expected_results - Вводим случайный набор символов, и проверяем, что поиск не выдает результатов, и пишет об этом сообщение
