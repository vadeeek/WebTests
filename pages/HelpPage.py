import allure
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class HelpPageLocators:
    SEARCH_FIELD = (By.XPATH, '//input[@type="search"]')
    ACTUAL_TODAY = (By.XPATH, '//a[contains(@href, "/help/segodnya-aktualno")]')
    REGISTRATION = (By.XPATH, '//a[contains(@href, "/help/registraciya")]')
    MY_PROFILE = (By.XPATH, '//a[contains(@href, "/help/moi-profil")]')
    COMMUNICATION = (By.XPATH, '//a[contains(@href, "/help/obshchenie")]')
    PROFILE_ACCESS = (By.XPATH, '//a[contains(@href, "/help/dostup-k-profilu")]')
    SECURITY = (By.XPATH, '//a[contains(@href, "/help/bezopasnost")]')
    GROUPS = (By.XPATH, '//a[contains(@href, "/help/gruppy")]')
    PAYED_FUNCTIONS = (By.XPATH, '//a[contains(@href, "/help/platnye-funkcii")]')
    SPAM = (By.XPATH, '//a[contains(@href, "/help/narusheniya-i-spam")]')
    GAMES_ANS_APPS = (By.XPATH, '//a[contains(@href, "/help/igry-i-prilojeniya")]')
    OTHER_SERVICES = (By.XPATH, '//a[contains(@href, "/help/drugie-servisy")]')
    IMPORTANT_INFORMATION = (By.XPATH, '//a[contains(@href, "/help/poleznaya-informaciya")]')
    ADVERTISEMENT_CABINET = (By.XPATH, '//a[contains(@href, "/help/reklamnyi-kabinet")]')


class HelpPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(HelpPageLocators.SEARCH_FIELD)
        self.find_element(HelpPageLocators.ACTUAL_TODAY)
        self.find_element(HelpPageLocators.REGISTRATION)
        self.find_element(HelpPageLocators.MY_PROFILE)
        self.find_element(HelpPageLocators.COMMUNICATION)
        self.find_element(HelpPageLocators.PROFILE_ACCESS)
        self.find_element(HelpPageLocators.SECURITY)
        self.find_element(HelpPageLocators.GROUPS)
        self.find_element(HelpPageLocators.PAYED_FUNCTIONS)
        self.find_element(HelpPageLocators.SPAM)
        self.find_element(HelpPageLocators.GAMES_ANS_APPS)
        self.find_element(HelpPageLocators.OTHER_SERVICES)
        self.find_element(HelpPageLocators.IMPORTANT_INFORMATION)
        self.find_element(HelpPageLocators.ADVERTISEMENT_CABINET)

    @allure.step('Скроллим страницу до нужного элемента')
    def scroll_to_item(self, locator):
        scroll_item = self.find_element(locator)
        ActionChains(self.driver).scroll_to_element(scroll_item).click(scroll_item).perform()