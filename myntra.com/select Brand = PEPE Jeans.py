""" Filtering only Brand= Pepe Jeans tshirts  kids=> boys => Pepe Jeans"""
from selenium.webdriver import Chrome
from time import sleep

driver = Chrome("./chromedriver")

driver.get("https://www.myntra.com/boys-tshirts")
sleep(5)

# click on the label "Pepe Jeans" to filterout all t-shirts with brand name = "Pepe Jeans"

driver.find_element_by_xpath("(//label[@class='vertical-filters-label common-customCheckbox'])[4]").click()
sleep(5)


# Read the brand of all the t-shirts
brands = driver.find_elements_by_xpath("//h3[@class='product-brand']")

for brand in brands:
    if brand.text == 'Pepe Jeans':
        print(brand.text)
        sleep(0.1)

    else:
        print(f"Other brands are getting displayed {brand.text}")

# ???????????????????????????????????? check once