""" Extracting t shirt name and discount of all discounted tshirts in kids section """
from selenium.webdriver import Chrome
from time import sleep

# driver = Chrome("./chromedriver")
driver = Chrome(r"C:\Users\Saurabh\Desktop\Python+Selenium\selenium_practice\chromedriver.exe")

driver.get("https://www.myntra.com/kids?f=Categories%3ATshirts%3A%3AGender%3Aboys%2Cboys%20girls")
sleep(5)

element_discount = driver.find_elements_by_xpath("//span[@class='product-discountPercentage']")

element_tshirts = driver.find_elements_by_xpath("//span[@class='product-discountPercentage']/../..//h4[@class='product-product']")

# getting the discount of all the discount elements
discount = [item.text for item in element_discount]

# tshirt names of all the discounted tshirts
tshirts_names = [item.text for item in element_tshirts]

# Building a list of tuples with tshirt-name and its discounted pair
actual_discount = [(name, price) for name, price in zip(tshirts_names, discount)]

print(actual_discount)




