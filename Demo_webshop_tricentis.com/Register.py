from selenium.webdriver import Chrome
from time import sleep

email_ = "stevejobs12@gmail.com"
password_ = "Steve123456"

# driver = Chrome("./chromedriver")
driver = Chrome(r"C:\Users\Saurabh\Desktop\Python+Selenium\selenium_practice\chromedriver.exe")

driver.get("http://demowebshop.tricentis.com")

driver.maximize_window()

driver.find_element_by_css_selector("a[class='ico-register']").click()
sleep(2)

# select Male
m = driver.find_element_by_css_selector("input[id='gender-male']")
m.click()
sleep(2)

# first_name = driver.find_element_by_css_selector("input[id='FirstName']")
first_name = driver.find_element_by_id("FirstName")
first_name.send_keys("Steve")
sleep(2)

last_name = driver.find_element_by_css_selector("input[name='LastName']")
last_name.send_keys("Jobs")
sleep(2)

email = driver.find_element_by_css_selector("input[id='Email']")
email.send_keys(email_)
sleep(2)

password = driver.find_element_by_css_selector("input[id='Password'")
password.send_keys(password_)
sleep(2)

con_password = driver.find_element_by_css_selector("input[id='ConfirmPassword']")
con_password.send_keys(password_)
sleep(2)

driver.find_element_by_css_selector("input[value='Register']").click()

driver.find_element_by_css_selector("input[value='Continue']").click()

driver.find_element_by_css_selector("a[class='account']").click()

