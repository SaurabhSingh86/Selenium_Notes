from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = Chrome(r"C:\Users\Saurabh\Desktop\Python+Selenium\selenium_practice\chromedriver.exe")
driver.get("http://demowebshop.tricentis.com")
driver.maximize_window()
sleep(2)


# Page Down
actions = ActionChains(driver)

# i want to page down two time then we use range other wise
# for _ in range(2):
#     actions.send_keys(Keys.PAGE_DOWN).perform()
#     sleep(2)


# Page Up
# actions = ActionChains(driver)
# actions.send_keys(Keys.PAGE_UP).perform()
# sleep(2)

# Arrow Down
# actions = ActionChains(driver)
# for _ in range(10):
#     actions.send_keys(Keys.ARROW_DOWN).perform()
#     sleep(1)

# # Arrow UP
# actions = ActionChains(driver)
# for _ in range(5):
#     actions.send_keys(Keys.ARROW_UP).perform()
#     sleep(1)
#
# # Tab
# actions = ActionChains(driver)
actions.send_keys(Keys.TAB).perform()
sleep(2)
#
# # Enter
# actions = ActionChains(driver)
# actions.send_keys(Keys.ENTER).perform()
# sleep(2)
#
# # ESC
# actions = ActionChains(driver)
# actions.send_keys(Keys.ESCAPE).perform()
