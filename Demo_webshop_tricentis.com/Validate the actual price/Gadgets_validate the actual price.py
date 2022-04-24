from selenium.webdriver import Chrome
from time import sleep

driver = Chrome("./chromedriver")

driver.get("http://demowebshop.tricentis.com")
# driver.maximize_window()
# sleep(2)

# Dictionary with Gadget name & expected prices
expected_prices = {"$25 Virtual Gift Card": 25.00,
                   "14.1-inch Laptop": 1590.00,
                   "Build your own cheap computer": 800.00,
                   "Build your own computer": 1200.00,
                   "Build your own expensive computer": 1800.00,
                   "Simple Computer": 800.00
                   }

for gadget, expected_price in expected_prices.items():
    xpath_ = f"//a[text()='{gadget}']/../..//span[@class='price actual-price']"
    actual_price = driver.find_element_by_xpath(xpath_).text
    if float(actual_price) == expected_price:
        print(f"{gadget}, Pass")
    else:
        print("Fail")
        print(f'The actual price of {gadget} gadget is {actual_price} and expected_price is {expected_price}')
    sleep(1)
