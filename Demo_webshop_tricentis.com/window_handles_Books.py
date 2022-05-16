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