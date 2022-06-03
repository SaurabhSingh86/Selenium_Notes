from selenium.webdriver import Chrome
from time import sleep
from selenium.common.exceptions import NoSuchElementException

driver = Chrome(r"C:\Users\Saurabh\Desktop\Python+Selenium\selenium_practice\chromedriver.exe")
driver.get("https://www.cleartrip.com/")
driver.maximize_window()
sleep(2)

# click on calendar
driver.find_element("xpath", "//div[@class='flex flex-middle flex-between p-relative homeCalender']").click()
sleep(1)

# _month = "November 2022"
# _day = "26"
#
# for _ in range(12):
#     try:
#         driver.find_element("xpath", )

# Method 2:
next_click_calendar = driver.find_element("css_selector", "svg[data-testid='rightArrow']")
month_year = driver.find_element("css_selector", "div[class='flex-1 ta-left']")


