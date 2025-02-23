from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    SECTION_LOGIN_BUTTON = (By.XPATH, '// *[ @ id = "login-6156265006"]')
    SECTION_LOGIN_BY_QR_BUTTON = (By.XPATH, '//*[@id="qrCode-6156265068"]')
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    LOGIN_BY_QR_BUTTON = (By.XPATH, '//*[@data-l="t,get_qr"]')
    CANT_LOGIN_BUTTON = (By.XPATH, '//*[@id="tabpanel-login-6156265006"]/form/div[4]/div[1]/a')
    REGISTER_BUTTON = (By.XPATH, '//*[@id="tabpanel-login-6156265006"]/form/div[4]/div[2]/a')
    LOGIN_BY_VK_BUTTON = (By.XPATH, '//*[@id="tabpanel-login-6156265006"]/form/div[4]/div[2]/div[2]/a[1]/i')
    LOGIN_BY_MAIL_RU_BUTTON = (By.XPATH, '//*[@id="tabpanel-login-6156265006"]/form/div[4]/div[2]/div[2]/a[2]/i')
    LOGIN_BY_GOOGLE_BUTTON = (By.XPATH, '//*[@id="tabpanel-login-6156265006"]/form/div[4]/div[2]/div[2]/a[3]/i')
    LOGIN_BY_YANDEX_BUTTON = (By.XPATH, '//*[@id="tabpanel-login-6156265006"]/form/div[4]/div[2]/div[2]/a[4]/i')
    LOGIN_BY_APPLE_BUTTON = (By.XPATH, '//*[@id="tabpanel-login-6156265006"]/form/div[4]/div[2]/div[2]/a[5]/i')

class LoginPageHelper(BasePage):
    pass