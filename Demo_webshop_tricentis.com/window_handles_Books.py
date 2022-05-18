# Requirements:
# Java Script Alert
# An Alert shows a custom messagae & a single button which dismiss the alert, labelled in most browsers as OK
# WebDriver can get the text from the popup & accept or dismiss these alerts.

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(r"C:\Users\Saurabh\Desktop\Python+Selenium\selenium_practice\chromedriver.exe")
driver.get("http://demowebshop.tricentis.com")
driver.maximize_window()
sleep(2)

# Click on "Search Button" without entering any Search keyword
driver.find_element("xpath", "//input[@value='Search']").click()
sleep(1)

# Get the text of the JavaScript Alert
print(driver.switch_to.alert.text)
sleep(2)

# click on OK
driver.switch_to.alert.accept()
