from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(r"C:\Users\Saurabh\Desktop\Python+Selenium\selenium_practice\chromedriver.exe")
driver.get("https://www.goibibo.com/")
driver.maximize_window()
sleep(2)

# click on calendar
driver.find_element("xpath", "//span[text()='Departure']").click()
