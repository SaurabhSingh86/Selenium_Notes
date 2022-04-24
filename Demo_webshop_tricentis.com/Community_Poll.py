from selenium.webdriver import Chrome
import time

driver = Chrome("./chromedriver")

driver.get("http://demowebshop.tricentis.com")
time.sleep(2)

driver.maximize_window()
time.sleep(2)

# Case 1:
# Select Good Radio button
# driver.find_element_by_id("pollanswers-2").click()
# time.sleep(2)
#
# vote = driver.find_element_by_id("vote-poll-1")
# vote.click()

# Case 2
# select each radio button one by one
ratings = ["Excellent", "Good", "Poor", "Very bad"]
for rating in ratings:
    # Dynamic X path
    driver.find_element_by_xpath(f"//label[text()='{rating}']/..//input[@type()='radio']").click()
    time.sleep(1)
