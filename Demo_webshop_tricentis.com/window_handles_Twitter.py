# Requirements:
# 1. Launch demowebshop
# 2. Click "Twitter" link at the footer of the webpage
# 3. "Twitter" page opens in new tab
# 4. get window handles & switch to twitter tab & enter some text in search field
# 5. switch back to parent window & click on "Register" link

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(r"C:\Users\Saurabh\Desktop\Python+Selenium\selenium_practice\chromedriver.exe")
driver.get("http://demowebshop.tricentis.com")
driver.maximize_window()
sleep(2)

# click on Twitter link present on the footer of the webpage
driver.find_element("xpath", "//a[text()='Twitter']").click()
sleep(5)

# Twitter page opens in a new tab in the browser
# in-order to switch the tab, get window handles
# window_handles return a list of window's id
handles = driver.window_handles

# switch to window handle of "Twitter"
driver.switch_to.window(handles[1])
sleep(2)

# Enter text in search text box on "Twitter" page
driver.find_element("xpath", "//input[@placeholder='Search Twitter']").send_keys("Galaxy")
sleep(2)

# switch back to parent window
driver.switch_to.window(handles[0])
sleep(2)


# click on "Register" link present on Demowebshop page
# driver.find_element("class_name", "ico-register").click() ????/ wrong way
driver.find_element("css selector", "a[class='ico-register']").click()
