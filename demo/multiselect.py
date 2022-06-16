""" selecting all item in multi-select"""

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select

# driver = Chrome("./chromedriver")
driver = Chrome(r"C:\Users\Saurabh\Desktop\Python+Selenium\selenium_practice\chromedriver.exe")
driver.get("file:///C:/Users/Saurabh/Desktop/Python+Selenium/selenium_practice/Selenium/demo.html")
driver.maximize_window()
sleep(2)

list_box = driver.find_element_by_id("multiple_cars")
s = Select(list_box)
all_options = s.options

# items = [item.text for item in all_options]
#
# for item in items:
#     s.select_by_visible_text(item)
#     sleep(0.5)


for item in all_options:
    s.select_by_visible_text(item.text)
    sleep(0.5)

