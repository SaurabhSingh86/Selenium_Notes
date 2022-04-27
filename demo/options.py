from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select

driver = Chrome("./chromedriver")
driver.get("file:///C:/Users/Saurabh/Desktop/Python+Selenium/selenium_practice/Selenium/demo.html")
driver.maximize_window()
sleep(2)

list_box = driver.find_element_by_id("standard_cars")
select = Select(list_box)

all_options = select.options

for item in all_options:
    print(item.text)
    sleep(1)


# Select car:
# Audi
# BMW
# Ford
# Honda
# Jaguar
# Land Rover
# Mercedes
# Mini
# Nissan
# Toyota
# Volvo