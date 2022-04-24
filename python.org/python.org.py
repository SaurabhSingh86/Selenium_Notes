from selenium.webdriver import Chrome
from time import sleep

driver = Chrome("./chromedriver")

driver.get(f"https://www.python.org/")
sleep(2)

driver.maximize_window()
sleep(2)

downloads = driver.find_element_by_xpath("//a[text()='Downloads']")
downloads.click()
sleep(2)

# click on Python 3.9.4
python_release = driver.find_element_by_xpath("//a[text()='Python 3.9.4']/../..//a[text()='Release Notes']")
python_release.click()

