# practice
from selenium.webdriver import Chrome
from time import sleep

#Lanuches a new chrome browser
driver = Chrome("./chromedriver")
sleep(2)

# navigate to demowebsop
driver.get("http://demowebshop.tricentis.com/")

driver.minimize_window()
sleep(2)

driver.maximize_window()
sleep(2)


current_title = driver.title

url = driver.current_url
print(url)

driver.close()
