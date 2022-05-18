from selenium.webdriver import Chrome
from time import sleep

# driver = Chrome("./chromedriver")
driver = Chrome(r"C:\Users\Saurabh\Desktop\Python+Selenium\selenium_practice\chromedriver.exe")

driver.get("file:///C:/Users/Saurabh/Desktop/Python+Selenium/selenium_practice/Selenium/demo.html")

driver.maximize_window()

""" 1. Check all the checkbox's"""

# using find_element
# checking all the checkboxes using dynamic
# dependent & independent
# languages = ["Ruby", "Java", "Perl", "Python", "C#", "JavaScript"]
# for language in languages:
#     # Dynamic xpath
#     driver.find_element_by_xpath(f"//td[text()='{language}']/..//input[@name='download']").click()
#     sleep(2)

# using find_elements

elements = driver.find_elements_by_name("download")
#
# for element in elements:
#     element.click()
#     sleep(1)

""" 2. Check all the checkbox's in reversed order"""

# method 1:
# for element in elements[::-1]:
#     element.click()
#     sleep(1)

# method 2:
# for element in reversed(elements):
#     element.click()
#     sleep(1)


""" 3. Check alternate checkbox's """
# for element in elements[::2]:
#     element.click()
#     sleep(0.5)


""" 4. Check first & last checkbox's """
elements[0].click()
sleep(1)
elements[-1].click()

