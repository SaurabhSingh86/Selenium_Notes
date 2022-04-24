from selenium.webdriver import Chrome
from time import sleep

driver = Chrome("./chromedriver")

driver.get("http://demowebshop.tricentis.com")
driver.maximize_window()
sleep(2)

driver.find_element_by_xpath("//a[contains(text(), 'Books')]").click()
sleep(2)

# Reference dictionary Maintaining the book name & expected price
expected_prices = {"Computing and Internet": 30.00,
                   "Copy of Computing and Internet EX": 30.00,
                   "Fiction": 35.00,
                   "Fiction EX": 35.00,
                   "Health Book": 27,
                   "Science": 67.00
                   }

for book, expected_price in expected_prices.items():
    actual_price = driver.find_element_by_xpath(f"//a[text()='{book}']/../..//span[@class='price actual-price']").text
    if float(actual_price) == expected_price:
        print("PASS")
    else:
        print("FAIL")
        print(f'The actual price of {book} book is {actual_price} and the expected price is {expected_price}')

