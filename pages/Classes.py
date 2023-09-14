from .base_page import BasePage
from .locators import AuthLocators
from .locators import RegLocators



class AuthPage(BasePage):

    def __init__(self, driver, timeout=3, ):
        super().__init__(driver, timeout)
        url = 'https://b2c.passport.rt.ru'
        driver.maximize_window()
        driver.get(url)

        self.tub_phone = driver.find_element(*AuthLocators.TAB_PHONE)
        self.tub_email = driver.find_element(*AuthLocators.TAB_MAIL)
        self.mail = driver.find_element(*AuthLocators.AUTH_LOGIN)
        self.auth_pass = driver.find_element(*AuthLocators.AUTH_PASS)
        self.btn_enter = driver.find_element(*AuthLocators.AUTH_BTN)
        self.tub_login = driver.find_element(*AuthLocators.TAB_LOGIN)
        self.tub_ls = driver.find_element(*AuthLocators.TAB_LS)
        self.forgot_password_link = driver.find_element(*AuthLocators.BTN_FORGOT_PASSWORD)
        self.register_link = driver.find_element(*AuthLocators.REGISTER_LINK)
        self.page_right = driver.find_element(*AuthLocators.PAGE_RIGHT)
        self.page_left = driver.find_element(*AuthLocators.PAGE_LEFT)
        self.card_of_auth = driver.find_element(*AuthLocators.CARD_OF_AUTH)
        self.tub_menu = driver.find_element(*AuthLocators.TAB_MENU)
        self.btn_vk = driver.find_element(*AuthLocators.BTN_VK)
        self.btn_ok = driver.find_element(*AuthLocators.BTN_OK)
        self.btn_ma = driver.find_element(*AuthLocators.BTN_MA)
        self.btn_ya = driver.find_element(*AuthLocators.BTN_YA)


    def find_other_element(self, by, location):
        return self.driver.find_element(by, location)

class RegPage(BasePage):
    def __init__(self, driver, timeout=3, ):
        super().__init__(driver, timeout)
        url = 'https://b2c.passport.rt.ru'
        driver.maximize_window()
        driver.get(url)
        driver.find_element(*AuthLocators.REGISTER_LINK).click()

        self.first_name = driver.find_element(*RegLocators.FIRST_NAME)
        self.last_name = driver.find_element(*RegLocators.LAST_NAME)
        self.adr_reg = driver.find_element(*RegLocators.ADR_REG)
        self.mail_reg = driver.find_element(*RegLocators.MAIL_REG)
        self.pass_reg = driver.find_element(*RegLocators.PASS_REG)
        self.pass_reg_confirm = driver.find_element(*RegLocators.PASS_REG_CONFIRM)
        self.btn_reg = driver.find_element(*RegLocators.BTN_REG)
        # self.page_left_registration = driver.find_element(*AuthLocators.page_left_registration)
        self.card_of_reg = driver.find_element(*RegLocators.CARD_OF_REG)
        self.user_agreement = driver.find_element(*RegLocators.USER_AGREEMENT)

        # self.container_first_name = driver.find_element(*AuthLocators.container_first_name)
        # self.container_last_name = driver.find_element(*AuthLocators.container_last_name)
        # self.container_password_confirm = driver.find_element(*AuthLocators.container_password_confirm)

    def find_other_element(self, by, location):
        return self.driver.find_element(by, location)