from selenium.webdriver import Chrome
from time import sleep

driver = Chrome("./chromedriver")

driver.get(f"https://www.python.org/")
driver.maximize_window()
sleep(5)

# get all the web elements which matches the xpath "//a" (all links)
links = driver.find_elements_by_xpath("//a")

# Method 1:
# # declare an empty list
# all_links = []
#
# # Loop through the list(links), get the text of each link and append the text to the list
#
# for link in links:
#     all_links.append(link.text.strip())
#
# print(all_links)

# Method 2: using list comprehension

# all_links = [link.text.strip() for link in links]
# print(all_links)