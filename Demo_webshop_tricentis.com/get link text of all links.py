from selenium.webdriver import Chrome
from time import sleep

driver = Chrome("./chromedriver")

driver.get("http://demowebshop.tricentis.com")
driver.maximize_window()
sleep(1)

# print link text of all the links present in the left
# navigation bar of demowebshop

xpath_ = "//div[@class='block block-category-navigation']//a"
links = driver.find_elements_by_xpath(xpath_)
for link in links:
    print(link.text)                # print(link.text, link)
    sleep(2)
