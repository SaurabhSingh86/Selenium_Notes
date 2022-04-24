from selenium.webdriver import Chrome
from time import sleep
import re

driver = Chrome("./chromedriver")

driver.get("https://services.smartbear.com/samples/TestComplete14/smartstore/sunglasses")
driver.maximize_window()
sleep(1)

footer_links = driver.find_elements_by_xpath("//div[@class='row sm-gutters']//a")
for link in footer_links:
    print(link.text)
    sleep(1)
