from selenium.webdriver import Chrome
from time import sleep
import re

driver = Chrome("./chromedriver")

driver.get("https://services.smartbear.com/samples/TestComplete14/smartstore/sunglasses")
driver.maximize_window()
sleep(2)

# dictionary with sunglasses name & expected price

expected_prices = {"Sunglasses Aero": 139.00,
                   "ORIGINAL COLLECTION": 149.00,
                   "Custom Sunglasses": 179.00
                   }

for sunglasses, expected_price in expected_prices.items():
    actual_price = driver.find_element_by_xpath(f"//span[text()='{sunglasses}']/../../..//span[@class='art-price']").text
    actual_price = re.findall(r"\d+\.\d+", actual_price)
    if float(actual_price[0]) == expected_price:                # ***************************************
        print(f'{sunglasses}, "Pass"')
    else:
        print(f'{sunglasses}, "Fail"')
        print(f"The actual price of {sunglasses} is {actual_price} and expected price is {expected_price}")

