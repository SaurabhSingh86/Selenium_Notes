# Requirements:
# 1.
# 2.
# 3.
# 4.

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = Chrome(r"C:\Users\Saurabh\Desktop\Python+Selenium\selenium_practice\chromedriver.exe")
driver.get("file:///C:/Users/Saurabh/Desktop/Python+Selenium/selenium_practice/Selenium/demo.html")
driver.maximize_window()
sleep(2)

actions = ActionChains(driver)

click_me = driver.find_element("id", "double-click")

actions.double_click(click_me).perform()
