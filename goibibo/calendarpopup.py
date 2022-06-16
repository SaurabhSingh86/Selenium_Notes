from selenium.webdriver import Chrome
from time import sleep
from selenium.common.exceptions import NoSuchElementException

driver = Chrome(r"C:\Users\Saurabh\Desktop\Python+Selenium\selenium_practice\chromedriver.exe")
driver.get("https://www.goibibo.com/")
driver.maximize_window()
sleep(2)

# click on calendar
driver.find_element("xpath", "//span[text()='Departure']").click()
month_ = "May 2023"
day_ = "20"

# ---------------------------------------------------------------------------------------------------------------
# # selecting the month (assuming that we can book a ticket only 12 months in advance)
# for _ in range(12):
#     try:
#         driver.find_element("xpath", f"//div[text()='{month_}']")
#         break
#     except NoSuchElementException:
#         driver.find_element("xpath", "//span[@aria-label='Next Month']").click()
#         sleep(0.1)
#         continue
#
# # Select day
# try:
#     driver.find_element("xpath", f"//div[text()={day_}]").click()
# except NoSuchElementException:
#     print("Invalid Date for the given month")
#
#
# # exection date = 20 - May 2022
# month_ = "July 2023"
# day_ = 20
# # Invalid Date for the given month

# ---------------------------------------------------------------------------------------------------------------
# click on calendar

next_click_button = driver.find_element_by_css_selector('span[class="DayPicker-NavButton DayPicker-NavButton--next"]')
month_year = driver.find_element("xpath", "//div[text()='June 2022']")

# month_
while month_year.text != month_:
    next_click_button.click()

driver.implicitly_wait(2)

# day_
calendar_date = driver.find_element("xpath", f"//p[text()='{day_}']")
calendar_date.click()

# click on 'Done' button
driver.find_element("xpath", "//span[text()='Done']").click()