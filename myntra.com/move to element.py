# Requirement:
# 1. Open myntra.com
# 2. click on profile
# 3. click on Login / profile

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

mobile_no = 9876543210

driver = Chrome(r"C:\Users\Saurabh\Desktop\Python+Selenium\selenium_practice\chromedriver.exe")
driver.get(r"https://www.myntra.com/")
driver.maximize_window()
sleep(2)

actions = ActionChains(driver)

profile = driver.find_element("xpath", "//span[text()='Profile']")

# Mouse hover on profile
actions.move_to_element(profile).perform()      # passing webelement as argument
sleep(1)

# click on "Login / signup"
driver.find_element("xpath", "//a[text()='login / Signup']").click()
sleep(1)

# Enter mobile no
driver.find_element("xpath", "//input[@class='form-control mobileNumberInput']").send_keys(mobile_no)
sleep(1)

# click button
click_button = driver.find_element("xpath", "//div[@class='submitBottomOption']")
click_button.click()

# for checking the information it'll take 30 seconds
sleep(32)
click_button.click()

