from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement

driver = Chrome("./chromedriver")
driver.get("file:///C:/Users/Saurabh/Desktop/Python+Selenium/selenium_practice/Selenium/loading.html")
driver.maximize_window()
sleep(2)


class _visibility_of_element_located(visibility_of_element_located):
    def __call__(self, driver):
        # call the parent (visibility_of_element_located) class __call__ method __call__ method of parent class
        # return a webelement if the element is present in the DOM and also visible on the webpage if one of the
        # above conditions is not satisfied, then __call__ method returns boolean False
        displayed = super().__call__(driver)
        # Below code checks if the return value of __call__ is of type WebElement
        # if the return type is WebElement, then check if it is enabled.
        if isinstance(displayed, WebElement):
            # is_enabled method returns boolean True if the element is enabled.
            # otherwise, is_enabled method return boolean False
            return displayed.is_enabled()
        # else:
        #     return False
        return displayed


# create an object instance to WebDriverWait class
wait = WebDriverWait(driver, timeout=10)

# wait until the firstname textbox is visible on the webpage
wait.until(_visibility_of_element_located(("name", "fname")))

# Enter "Hello world" in firstname textbox
driver.find_element_by_name("fname").send_keys("Hello world")
