import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=ru")
    driver = webdriver.Remote(command_executor="http://31.129.111.252:4444", options=options)
    yield driver # поставили на паузу и не продолжать код, сессия завершилась - завершился браузер 👇
    if driver:
        driver.quit()