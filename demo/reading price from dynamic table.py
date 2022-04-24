from selenium.webdriver import Chrome
from time import sleep

driver = Chrome("./chromedriver")

driver.get("file:///C:/Users/Saurabh/Desktop/Python+Selenium/selenium_practice/Selenium/demo.html")
driver.maximize_window()
sleep(1)

companies = ["AAPL", "MSFT", "AA", "FB"]

# print the headers (company names)
for company in companies:
    print(f'{company:>15}', end="")

# print an empty line after headers
print()
print('-' * 65)

# while loop to monitor the share price every 2 seconds
while True:
    for company in companies:
        share_price = driver.find_element_by_xpath(f"//td[text()='{company}']/..//td[@class='price']").text
        print(f'{share_price:>15}', end="")
    print()
    sleep(2)
