# Requirements:
# 1. Open naukri.com
# 2. click on job search
# 3. Jobs by skills
# 4. PYTHON JOBS
email_id = "saurabhsingh8602@gmail.com"

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = Chrome(r"C:\Users\Saurabh\Desktop\Python+Selenium\selenium_practice\chromedriver.exe")
driver.get("https://www.naukri.com")
driver.maximize_window()
sleep(2)

# click on login button
driver.find_element("id", "login_Layer").click()
sleep(2)

# click on sign in with google
# driver.find_element_by_link_text("Sign in with Google").click() ??????????/ this one not working
driver.find_element("xpath", "//div[@class='google']").click()

# handeling multiple window
handler = driver.window_handles

# switch to window handle of sign in window
driver.switch_to.window(handler[1])
sleep(2)

# Enter email id
driver.find_element("id", "identifierId").send_keys(email_id)
sleep(1)

# click on next button
driver.find_element("xpath", "//span[text()='Next']").click()
