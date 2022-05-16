from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver = Chrome(r"C:\Users\Saurabh\Desktop\Python+Selenium\selenium_practice\chromedriver.exe")
driver.get("file:///C:/Users/Saurabh/Desktop/Python+Selenium/selenium_practice/Selenium/demo.html")
driver.maximize_window()
sleep(2)

# actions = ActionChains(driver)
#
# first_row = driver.find_element("id", "firstname")
# actions.send_keys(first_row).perform()

# not working ?????????????????