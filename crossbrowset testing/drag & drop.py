# Requirement: perform drag & drop action of source element onto target element

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = Chrome(r"C:\Users\Saurabh\Desktop\Python+Selenium\selenium_practice\chromedriver.exe")
driver.get("https://crossbrowsertesting.github.io/drag-and-drop.html")
driver.maximize_window()
sleep(2)

# store box A as source element
source_element = driver.find_element("id", "draggable")

# store box B as target element
target_element = driver.find_element("id", "droppable")

# perform drag & drop action of source element onto target element
actions = ActionChains(driver)
actions.drag_and_drop(source_element, target_element).perform()