import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome() # запустили браузер и пускай дальше webdriver с ним работает и делает, что хочет
    yield driver # поставили на паузу и не продолжать код, сессия завершилась - завершился браузер 👇
    driver.quit()