# in confirm box user can choose either "OK" button or "Cancel" button

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(r"C:\Users\Saurabh\Desktop\Python+Selenium\selenium_practice\chromedriver.exe")
driver.get("file:///C:/Users/Saurabh/Desktop/Python+Selenium/selenium_practice/Selenium/demo.html")
driver.maximize_window()
sleep(2)

# Get all the checkboxes
elements = driver.find_element("xpath", "//input[@class='alert']")
print(elements)

# Check all the checkboxes
for element in elements:
    element.click()
    sleep(1)

#
