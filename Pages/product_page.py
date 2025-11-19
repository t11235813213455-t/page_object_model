from .base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click() 
       
    def get_book_name(self):
        return self.get_text_of_element(*ProductPageLocators.BOOK_NAME)

    def get_price(self):   
        return self.get_text_of_element(*ProductPageLocators.PRICE)

    def should_be_msg_about_adding_to_basket(self, book_name, price):
        msg = self.get_text_of_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING_TO_BASKET)
        price_msg = self.get_text_of_element(*ProductPageLocators.PRICE_MSG)
        assert "has been added to your basket." in msg, "Message 'has been added to your basket' is absent" 
        assert book_name in msg, "Book title in the message is incorrect"
        assert price in price_msg, "Book price in the message is incorrect"
