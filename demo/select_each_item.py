from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select

# driver = Chrome("./chromedriver")
driver = Chrome(r"C:\Users\Saurabh\Desktop\Python+Selenium\selenium_practice\chromedriver.exe")

driver.get("file:///C:/Users/Saurabh/Desktop/Python+Selenium/selenium_practice/Selenium/demo.html")
driver.maximize_window()
sleep(2)

# list_box = driver.find_element_by_id("standard_cars")
list_box = driver.find_element("id", "multiple_cars")

s = Select(list_box)
all_options = s.options


""" selecting each item in the list one by one """

for item in all_options:
    s.select_by_visible_text(item.text)
    sleep(0.5)

"""deselecting each item in the list one by one """
for item in all_options:
    s.deselect_by_visible_text(item.text)
    sleep(0.5)

""" selecting each item in the list one by one in Reversed order"""

# Method 1: using slicing
# for item in all_options[::-1]:
#     s.select_by_visible_text(item.text)
#     sleep(1)

# Method 2: using reversed
# for item in reversed(all_options):
#     s.select_by_visible_text(item.text)
#     sleep(1)


""" select last item of the list box"""

# get the text of each options to select last item in the list box using visible text
# items = [item.text for item in all_options]
#
# s.select_by_visible_text(items[-1])


""" print index at which the "Mercedes" is present """
# items = [item.text for item in all_options]
#
# for index, item in enumerate(items):
#     if item == 'Mercedes':
#         print(f'{item} is present at index {index}')

