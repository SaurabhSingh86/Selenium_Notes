""" List of link text of all the links if the text contains "Python" word in it """

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome("./chromedriver")

driver.get(f"https://www.python.org/")
driver.maximize_window()
sleep(5)

# get all the web elements which matches the xpath "//a" (all links)
links = driver.find_elements_by_xpath("//a")

python_links = []

for link in links:
    link_of_link = link.text
    if "Python" in link_of_link:
        python_links.append(link.text.strip())

print(python_links)
