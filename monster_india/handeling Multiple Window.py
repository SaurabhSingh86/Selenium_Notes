# Requirements:
# 1. Launch monster.com
# 2. Search Pyton Jobs.
# 3. Click on first job title in search result
# 4. click apply button

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(r"C:\Users\Saurabh\Desktop\Python+Selenium\selenium_practice\chromedriver.exe")
driver.get("https://www.monsterindia.com/")
driver.maximize_window()
sleep(2)

# search "Python" jobs
driver.find_element("id", "SE_home_autocomplete").send_keys("Python")
sleep(1)

driver.find_element("xpath", "(//strong[text()='Python'])[1]").click()
sleep(2)


# click on search button
driver.find_element("xpath", "//input[@value='Search']").click()
sleep(5)

driver.find_element("xpath", "(//div[@class='job-tittle']/h3/a)[1]").click()
sleep(5)

# Get the window handles
handles = driver.window_handles

# Switch to child browser
driver.switch_to.window(handles[0])
sleep(2)



# click apply button
driver.find_element("xpath", "(//button[text()='APPLY'])[1]").click()
sleep(2)

