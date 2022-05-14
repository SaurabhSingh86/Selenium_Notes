
from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select
import csv
import re
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from Selenium_Wrapper import SeleniumWrapper


class _visibility_of_element_located(visibility_of_element_located):
    def __init__(self, locator):
        super().__init__(locator)

    def __call__(self, driver):
        result = super().__call__(driver)
        # Checking if __call__ has returned a WebElement?
        if isinstance(result, WebElement):
            return result.is_enabled()
        return result


def wait(func):
    def wrapper(*args, **kwargs):  # args = (self, ("id", "multiple_cars"))
        instance = args[0]
        locator = args[1]  # get the inner tuple
        # Wait (3 Conditions)
        wait = WebDriverWait(instance.driver, 10)
        v = _visibility_of_element_located(locator)
        wait.until(v)
        return func(*args, **kwargs)  # original func is executed (click_element, enter_text)

    return wrapper


# class SeleniumWrapper:
#     def __init__(self, driver):
#         self.driver = driver
#
#     @wait  # enter_text = wait(enter_text)
#     def enter_text(self, locator, *, value):
#         self.driver.find_element(*locator).send_keys(value)
#
#     @wait  # click_element = wait(click_element)
#     def click_element(self, locator):
#         self.driver.find_element(*locator).click()
#
#     @wait  # select_item = wait(select_item)
#     def select_item(self, locator, *, item):
#         element = self.driver.find_element(*locator)
#         s = Select(element)
#         if isinstance(item, str):
#             s.select_by_visible_text(item)
#         elif isinstance(item, int):
#             s.select_by_index(item)
#         else:
#             raise TypeError(f"Invalid Type {item}")
#
#     @wait
#     def select_items(self, locator, *, items):
#         for _item in items:
#             try:
#                 self.select_item(locator, item=_item)
#             except NoSuchElementException:
#                 print(f"Could not find item {_item}")
#                 continue


driver = Chrome(r"C:\Users\Saurabh\Desktop\Python+Selenium\selenium_practice\chromedriver.exe")
driver.get("file:///C:/Users/Saurabh/Desktop/Python+Selenium/selenium_practice/Selenium/demo.html")
sleep(5)


# import Selenium_Wrapper

s = SeleniumWrapper(driver)

# click_element(("link text", "Register"))
s.select_items(("id", "multiple_cars"), items=['Mercedes', 'Creta', 'BMW', 10])

