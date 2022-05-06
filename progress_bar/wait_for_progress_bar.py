from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = Chrome("./chromedriver")
driver.get("file:///C:/Users/Saurabh/Desktop/Python+Selenium/selenium_practice/Selenium/progressbar.html")
driver.maximize_window()
sleep(2)

# click on "click me" button on the demo webpage
driver.find_element_by_xpath("//button[text()='Click Me']").click()

wait = WebDriverWait(driver, timeout=30)

# wait until the progress bar is loaded completely (100%) and visible on the webpage
wait.until(expected_conditions.visibility_of_element_located(("xpath", "//div[text()='100%']")))
print("Done!")


# timeout=10        => raise TimeoutException(message, screen, stacktrace)
# timeout=20        => raise TimeoutException(message, screen, stacktrace)
# timeout=30        => Done!