from Pages.main_page import MainPage
from Pages.base_page import BasePage
from Pages.login_page import LoginPage
from Pages.product_page import ProductPage
import time
from selenium.common.exceptions import NoSuchElementException


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)    
    page.open()   
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_msg_about_adding_to_basket(page.get_book_name(), page.get_price())
