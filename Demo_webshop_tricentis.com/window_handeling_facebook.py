# Requirements:
# 1. Launch demowebshop
# 2. Navigate to Books Page
# 3. click on one of the book tittle
# 4. click on "facebook" icon
# 5. Enter Email & close the "Facebook" popup window

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(r"C:\Users\Saurabh\Desktop\Python+Selenium\selenium_practice\chromedriver.exe")
driver.get("http://demowebshop.tricentis.com")
driver.maximize_window()
sleep(2)

# Navigate to Books Page
driver.find_element("xpath", "//a[contains(text(),'Books')]").click()
sleep(2)

# click on "Fiction" books
driver.find_element("xpath", "//a[text()='Fiction']").click()
sleep(5)

# click on "Facebook" icon
driver.find_element("xpath", "//a[@title='Facebook']").click()
sleep(2)

# Get all window handles
handles = driver.window_handles

# Switch to facebook window
driver.switch_to.window(handles[1])
sleep(2)

# Enter email
driver.find_element("id", "email").send_keys("steve@jobs.com")
sleep(2)

driver.close()

# Switch back to Parent Window & close
driver.switch_to.window(handles[0])
sleep(2)

driver.close()

