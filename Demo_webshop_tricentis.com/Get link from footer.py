from selenium.webdriver import Chrome
from time import sleep

driver = Chrome("./chromedriver")

driver.get("http://demowebshop.tricentis.com")
sleep(1)

# print link text of all the link present in the footer
footer_links = driver.find_elements_by_xpath("//div[@class='footer-menu-wrapper']//a")
for link in footer_links:
    print(link.text)
    sleep(1)