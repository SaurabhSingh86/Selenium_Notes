from selenium.webdriver import Chrome
from time import sleep

email_ = "stevejobs12@gmail.com"
password_ = "Steve123456"

driver = Chrome("./chromedriver")

driver.get("http://demowebshop.tricentis.com")

driver.maximize_window()
sleep(1)

#login
# driver.find_element_by_css_selector("a[class='ico-login]").click()
driver.find_element_by_xpath("//a[text()='Log in']").click()
sleep(2)

driver.find_element_by_css_selector("input[id='Email']").send_keys(email_)
sleep(2)

driver.find_element_by_css_selector("input[id='Password']").send_keys(password_)
sleep(2)

# Remember me (checkbox)
driver.find_element_by_css_selector("input[id='RememberMe']").click()
sleep(1)

driver.find_element_by_css_selector("input[value='Log in']").click()
