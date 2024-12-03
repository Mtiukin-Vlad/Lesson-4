import time
import pytest
from selenium import webdriver

# Фикстура для запуска браузера (chrome) для каждого класса
@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")  # Сообщение о начале запуска браузера
    browser = webdriver.Chrome()  # Инициализация браузера Chrome
    yield browser  # Возвращаем браузер для использования в тестах
    print("\nquit browser..")  # Сообщение о завершении работы с браузером
    browser.quit()  # Закрытие браузера

# Фикстура для запуска второго экземпляра браузера (chrome) для каждого класса
@pytest.fixture(scope="class")
def browser2():
    print("\nstart browser for test..")  # Сообщение о начале запуска браузера
    browser = webdriver.Chrome()  # Инициализация браузера Chrome
    yield browser  # Возвращаем браузер для использования в тестах
    print("\nquit browser..")  # Сообщение о завершении работы с браузером
    browser.quit()  # Закрытие браузера

# Фикстура для добавления времени ожидания (30 секунд) после тестов
@pytest.fixture(scope="class")
def fix_sleeps():
    yield  # Выполняется перед тестом
    print("\nquit browser..")  # Сообщение о завершении работы с браузером
    time.sleep(30)  # Ожидание 30 секунд после завершения теста

# Функция для добавления параметров командной строки в pytest
import pytest
from selenium import webdriver

def pytest_addoption(parser):
    # Добавление параметра для выбора браузера
    parser.addoption('--browser_name1', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    # Добавление параметра для выбора языка интерфейса, с значением по умолчанию "en"
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: ru, hu, en. Default is 'en'")

# Фикстура для запуска браузера (chrome или firefox) на основе параметра командной строки
@pytest.fixture(scope="function")
def browser1(request):
    # Получение параметра для выбора браузера
    browser_name = request.config.getoption("--browser_name1")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")  # Сообщение о запуске Chrome
        browser = webdriver.Chrome()  # Инициализация Chrome
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")  # Сообщение о запуске Firefox
        browser = webdriver.Firefox()  # Инициализация Firefox
    else:
        # Ошибка, если выбран неверный браузер
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser  # Возвращаем браузер для использования в тестах
    print("\nquit browser..")  # Сообщение о завершении работы с браузером
    browser.quit()  # Закрытие браузера

# Фикстура для получения языка интерфейса из параметра командной строки
@pytest.fixture(scope="function")
def language(request):
    # Получение параметра для выбора языка
    language = request.config.getoption("--language")
    yield language  # Возвращаем выбранный язык
