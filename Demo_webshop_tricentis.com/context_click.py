from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = Chrome(r"C:\Users\Saurabh\Desktop\Python+Selenium\selenium_practice\chromedriver.exe")
driver.get("http://demowebshop.tricentis.com")
driver.maximize_window()
sleep(2)

# Store "register" link web element
register = driver.find_element("css selector", "a[class='ico-register']")

actions = ActionChains(driver)
actions.context_click(register).perform()


