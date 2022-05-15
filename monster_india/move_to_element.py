# Requirements:
# 1. Open Monsterindia.com
# 2. click on job search
# 3. Jobs by skills
# 4. PYTHON JOBS

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = Chrome(r"C:\Users\Saurabh\Desktop\Python+Selenium\selenium_practice\chromedriver.exe")
driver.get("https://www.monsterindia.com/")
driver.maximize_window()
sleep(5)

actions = ActionChains(driver)

# Job Search
job_search = driver.find_element("xpath", "//a[text()='Job search']")

actions.move_to_element(job_search).perform()
sleep(2)

# Job by Skills
job_by_title = driver.find_element("xpath", "//a[text()='Jobs by Skills']")

actions.move_to_element(job_by_title).perform()
sleep(2)

# Choose Python Jobs
python_jobs = driver.find_element("xpath", "//a[contains(text(), 'Python Jobs')]")

actions.move_to_element(python_jobs).perform()
sleep(2)

python_jobs.click()

