from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from time import sleep

driver = Chrome("./chromedriver")
driver.get("file:///C:/Users/Saurabh/Desktop/Python+Selenium/selenium_practice/Selenium/demo.html")
sleep(2)

list_box = driver.find_element_by_id("multiple_cars")
s = Select(list_box)

print(s.is_multiple)

# True