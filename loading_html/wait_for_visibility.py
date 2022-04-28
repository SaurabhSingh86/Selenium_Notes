from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

driver = Chrome("./chromedriver")
driver.get("file:///C:/Users/Saurabh/Desktop/Python+Selenium/selenium_practice/Selenium/loading.html")
driver.maximize_window()

# create an object instance to WebDriverWait class
wait = WebDriverWait(driver, timeout=15)

# wait until the firstname text box is visible on the webpage
wait.until(expected_conditions.visibility_of_element_located(("name", "fname")))

# Enter "Hello World" in firstname textbox
driver.find_element_by_name("fname").send_keys("Hello World")


# timeout=10        => raise TimeoutException(message, screen, stacktrace)
# timeout=15        => execute succesfully