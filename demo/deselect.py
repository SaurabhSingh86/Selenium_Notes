from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select

driver = Chrome("./chromedriver")
driver.get("file:///C:/Users/Saurabh/Desktop/Python+Selenium/selenium_practice/Selenium/demo.html")
driver.maximize_window()
sleep(2)

list_box = driver.find_elements_by_id("multiple_cars")
s = Select(list_box)

# deselect by visible text
s.deselect_by_visible_text("Audi")
sleep(2)

# deselect by index
s.deselect_by_index(2)
sleep(2)

# deselect by value
s.deselect_by_value("for")
