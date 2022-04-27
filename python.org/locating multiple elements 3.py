""" List of tuples of link text of all the links if the text contains "Python" word in it & corresponding value of
"href" attribute """

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome("./chromedriver")

driver.get(f"https://www.python.org/")
driver.maximize_window()
sleep(5)

# Get all the links present on the webpage
links = driver.find_elements_by_xpath("//a")

# declare an empty list
urls = []

# loop through the list(links)
for link in links:
    link_text = link.text
    # check if the link text has word "Python" in it using 'in' operator
    # if the link text has "Python" sub-string in it, get the value of 'href' attribute
    if "Python" in link_text:
        value_href = link.get_attribute("href")
        # append a tuple of link text and value of 'href' attribute to the list
        urls.append((value_href, link_text))

for url in urls:
    # print a tuple of url and its link text pair,
    print(url)