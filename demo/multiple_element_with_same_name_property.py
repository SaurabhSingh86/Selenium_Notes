from selenium.webdriver import Chrome
from time import sleep

driver = Chrome("./chromedriver")

driver.get("file:///C:/Users/Saurabh/Desktop/Python+Selenium/selenium_practice/Selenium/demo.html")

driver.maximize_window()
sleep(1)

# finding all the text boxes using find_elements_by_xpath()
boxes = driver.find_elements_by_xpath("//input[@name='fname']")

# text to be edited in each text field
# contents = ["hai", "hello", "welcome", "to", "Python", "world", "Pycharm", "NodeJS", "Git"]
#
# Interacting between two different lists in parallel
# for box, content in zip(boxes, contents):
#     box.send_keys(content)
#     sleep(1)

# case 2
contents = ["hai", "hello", "welcome", "to", "Python", "world", "Pycharm", "NodeJS"]
for box, content in zip(boxes, contents):
    box.send_keys(content)
    sleep(1)