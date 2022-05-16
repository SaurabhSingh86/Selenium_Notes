""" Select a Health book """

from selenium.webdriver import Chrome
from time import sleep

email_ = "stevejobs12@gmail.com"
password_ = "Steve123456"

# driver = Chrome("./chromedriver")
driver = Chrome(r"C:\Users\Saurabh\Desktop\Python+Selenium\selenium_practice\chromedriver.exe")

driver.get("http://demowebshop.tricentis.com")

driver.maximize_window()
sleep(1)

books = driver.find_element_by_xpath("//a[contains(text(), 'Books')]")
books.click()
sleep(2)

# select Health book as a cart
# driver.find_element_by_xpath("//a[text()='Health Book']").click()
# sleep(2)
#
# driver.find_element_by_css_selector("input[id='add-to-cart-button-22']").click()
# sleep(2)

# add to cart
# driver.find_element_by_xpath("//span[text()='Shopping cart']").click()
# driver.find_element_by_css_selector("span[class='cart-label']").click()
# sleep(2)


# Add to cart button of "Health", "Fiction", "Computing and internet"
books = ["Health Book", "Fiction", "Computing and Internet"]

for book in books:
    driver.find_element_by_xpath(f"//a[text()='{book}']/../..//input[@value='Add to cart']").click()
    sleep(2)

sleep(2)
# shopping cart
driver.find_element_by_xpath("//span[text()='Shopping cart']").click()
# driver.find_element_by_css_selector("span[class='cart-label']").click()
sleep(2)

# update the quantity of each itme 2 items each (all books has 2 no of copies)
for book in books:
    quantity = driver.find_element_by_xpath(f"//a[text()='{book}']/../..//input[@value='1']")
    quantity.clear()
    quantity.send_keys("2")
    sleep(1)


# remove "fiction book" from the shopping cart
for book in books:
    if book == 'Fiction':
        driver.find_element_by_xpath(f"//a[text()='{book}']/../..//input[@type='checkbox']").click()
        sleep(1)


driver.quit()