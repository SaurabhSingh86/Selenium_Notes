from selenium.webdriver import Chrome
from time import sleep

driver = Chrome("./chromedriver")

driver.get("file:///C:/Users/Saurabh/Desktop/Python+Selenium/selenium_practice/Selenium/demo.html")

driver.maximize_window()

# checking all the checkboxes using dynamic
# dependent & independent
languages = ["Ruby", "Java", "Perl", "Python", "C#", "JavaScript"]
for language in languages:
    # Dynamic xpath
    driver.find_element_by_xpath(f"//td[text()='{language}']/..//input[@name='download']").click()
    sleep(2)

