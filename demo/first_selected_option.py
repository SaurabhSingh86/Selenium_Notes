from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select

driver = Chrome(r"C:\Users\Saurabh\Desktop\Python+Selenium\selenium_practice\chromedriver.exe")
driver.get("file:///C:/Users/Saurabh/Desktop/Python+Selenium/selenium_practice/Selenium/demo.html")
driver.maximize_window()
sleep(2)

list_box = driver.find_element("id", "standard_cars")

s = Select(list_box)

s.select_by_visible_text('Mercedes')
s.select_by_visible_text('Ford')

currently_selected_option = s.first_selected_option.text
print(currently_selected_option)

