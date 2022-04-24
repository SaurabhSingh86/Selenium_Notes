from selenium.webdriver import Chrome
from time import sleep

driver = Chrome("./chromedriver")

driver.get("http://demowebshop.tricentis.com")
sleep(1)

driver.maximize_window()
sleep(2)

books = driver.find_element_by_xpath("//a[contains(text(),'Books')]")
books.click()

sleep(2)

