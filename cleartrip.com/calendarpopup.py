from selenium.webdriver import Chrome
from time import sleep
from selenium.common.exceptions import NoSuchElementException

driver = Chrome(r"C:\Users\Saurabh\Desktop\Python+Selenium\selenium_practice\chromedriver.exe")
driver.get("https://www.cleartrip.com/")
driver.maximize_window()
sleep(5)

# click on calendar
driver.find_element("xpath", "//button[@class='flex flex-middle flex-between t-all fs-2 focus:bc-secondary-500 bg-transparent bc-neutral-100 c-pointer pr-2 pl-3 pt-2 pb-2 ba br-4 h-8 c-neutral-900']").click()
driver.implicitly_wait(2)


# Method 1:

month_ = "November 2022"
day_ = "26"
next_click_calendar = driver.find_element_by_css_selector("svg[data-testid='rightArrow']")
month_year = driver.find_element("xpath", "//div[text()='June 2022']")

while month_year.text != month_:
    next_click_calendar.click()

driver.implicitly_wait(2)

driver.find_element("xpath", f'//div[text()="{day_}"]').click()


# Method 2:
# _month = "November 2022"
# _day = "26"
#
# for _ in range(12):
#     try:
#         driver.find_element("xpath", f"//div[text()='{_month}']/../..//div[text()='{_day}']").click()
#     except NoSuchElementException:
#         driver.find_element_by_css_selector("svg[data-testid='rightArrow']").click()
#         sleep(1)
#         continue


