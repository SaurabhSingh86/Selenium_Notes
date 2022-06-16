# Requirements:
# 1. Open Monsterindia.com
# 2.
# 3.
# 4.

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = Chrome(r"C:\Users\Saurabh\Desktop\Python+Selenium\selenium_practice\chromedriver.exe")
driver.get("https://www.monsterindia.com/")
driver.maximize_window()
driver.implicitly_wait(5)

# upload resume
driver.find_element("xpath", "//span[text()='Upload Resume']").send_keys("C:\Users\Saurabh\Desktop\Saurabh Singh Resume.pdf")
sleep(2)

# handles = driver.window_handles
#
# # switch to child browser
# driver.switch_to.window(handles[1])
#
# #
# driver.find_element("id", "file-upload").click()

