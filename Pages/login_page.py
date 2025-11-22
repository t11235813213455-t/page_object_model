from .base_page import BasePage
from .locators import BasePageLocators
from .locators import MainPageLocators
from .locators import LoginPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "URL address is incorrect"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is absent"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is absent"

    def register_new_user(self, email, password):
        timeout = 5
        login_link = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(BasePageLocators.LOGIN_LINK))
        login_link.click()

        email_field = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        email_field.send_keys(email)

        password_field = self.browser.find_element(*LoginPageLocators.REG_PASS1)
        password_field.send_keys(password)

        confirm_password_field = self.browser.find_element(*LoginPageLocators.REG_PASS2)
        confirm_password_field.send_keys(password)

        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

        #waiting until user is created and logged in
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(LoginPageLocators.ACCOUNT_LINK))

    def login_user(self, email, password):
        timeout = 5
        login_link = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(BasePageLocators.LOGIN_LINK))
        login_link.click()

        email_field = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        email_field.send_keys(email)

        password_field = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        password_field.send_keys(password)

        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

        #waiting until user is logged in
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(LoginPageLocators.ACCOUNT_LINK))
