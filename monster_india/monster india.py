from selenium.webdriver import Chrome
from time import sleep
import re

driver = Chrome("./chromedriver")

driver.get("https://www.monsterindia.com/")
driver.maximize_window()
sleep(1)

driver.find_element_by_xpath("//input[@id='SE_home_autocomplete']").send_keys("Python")

driver.find_element_by_xpath("//input[@value='Search']").click()
