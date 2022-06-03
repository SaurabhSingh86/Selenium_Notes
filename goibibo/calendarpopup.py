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

# selecting the month (assuming that we can book a ticket only 12 months in advance)
for _ in range(12):
    try:
        driver.find_element("xpath", f"//div[text()='{month_}']")
        break
    except NoSuchElementException:
        driver.find_element("xpath", "//span[@aria-label='Next Month']").click()
        sleep(0.1)
        continue

# Select day
try:
    driver.find_element("xpath", f"//div[text()={day_}]").click()
except NoSuchElementException:
    print("Invalid Date for the given month")


# exection date = 20 - May 2022
month_ = "July 2023"
day_ = 20
# Invalid Date for the given month

