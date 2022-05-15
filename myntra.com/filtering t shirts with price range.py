""" filtering t-shirts with price range between Rs. 1354 to Rs. 2569"""
from selenium.webdriver import Chrome
from time import sleep
import re

# driver = Chrome("./chromedriver")
driver = Chrome(r"C:\Users\Saurabh\Desktop\Python+Selenium\selenium_practice\chromedriver.exe")

driver.get("https://www.myntra.com/boys-tshirts")
sleep(5)

# click on the label Rs. 1354 to Rs. 2569
driver.find_element_by_xpath("(//label[@class='common-customCheckbox vertical-filters-label'])[2]").click()
sleep(5)

# get all the price tag elements
price_tag_element = driver.find_elements_by_xpath("//div[@class='product-price']")

# for each price tag element, read the text, typecast to float and check if the price falls in the expected range
for price in price_tag_element:
    temp = price.text
    parts = re.findall(r'\d+', temp)
    actual_price = float(parts[0])
    if actual_price >= 1354 and actual_price <= 2569:
        print("Pass")
    else:
        print(actual_price)
        print("Fail")
