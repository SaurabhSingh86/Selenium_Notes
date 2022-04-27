from selenium.webdriver import Chrome
from time import sleep
import re

driver = Chrome("./chromedriver")

driver.get("https://services.smartbear.com/samples/TestComplete14/smartstore")
driver.maximize_window()
sleep(1)

images = driver.find_elements_by_xpath("//img")
for image in images:
    print(image.get_attribute("alt"))
    sleep(0.5)
