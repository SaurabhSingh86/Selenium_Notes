from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select

# driver = Chrome("./chromedriver")
driver = Chrome(r"C:\Users\Saurabh\Desktop\Python+Selenium\selenium_practice\chromedriver.exe")


driver.get("file:///C:/Users/Saurabh/Desktop/Python+Selenium/selenium_practice/Selenium/demo.html")
driver.maximize_window()
sleep(2)

select_car = driver.find_element_by_id("standard_cars")
select_ = Select(select_car)


# Method 1: select by visible_text
# select_.select_by_visible_text("Jaguar")
# sleep(2)
#
# select_.select_by_visible_text("Honda")
# sleep(2)
#
# select_.select_by_visible_text("Land Rover")

# Method 2: select_by_index
# select_.select_by_index(5)
# sleep(2)
#
# select_.select_by_index(4)
# sleep(2)
#
# select_.select_by_index(6)

# Method 3: select_by_value
select_.select_by_value("hda")
sleep(1)

select_.select_by_value("jgr")
sleep(1)

select_.select_by_value("lr")
sleep(1)