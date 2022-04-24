from selenium.webdriver import Chrome
from time import sleep

driver = Chrome("./chromedriver")

driver.get("https://www.nseindia.com/market-data/pre-open-market-cm-and-emerge-market")
driver.maximize_window()
sleep(2)

companies = ["TCS", "WIPRO", "MARUTI"]

# print the headers(company names)
for company in companies:
    print(f'{company:>15}', end=" ")

# print an empty line after header
print()
print('-' * 55)

# while loop to monitor the share price every 5 seconds (infinite loop)
while True:
    for company in companies:
        share_price = driver.find_element_by_xpath(f"//a[text()='{company}']/../..//td[7]").text
        print(f'{share_price:>15}', end=" ")
    print()
    sleep(2)

