from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select

# driver = Chrome("./chromedriver")
driver = Chrome(r"C:\Users\Saurabh\Desktop\Python+Selenium\selenium_practice\chromedriver.exe")

driver.get("file:///C:/Users/Saurabh/Desktop/Python+Selenium/selenium_practice/Selenium/demo.html")
driver.maximize_window()
sleep(2)

list_box = driver.find_element_by_id("multiple_cars")
s = Select(list_box)

s.select_by_visible_text("Jaguar")
s.select_by_visible_text("Audi")
s.select_by_visible_text("Volvo")

# Returns list of all the options that are currently selected in multi-select listbox
all_sel_opt = s.all_selected_options

# print text of each option
for item in all_sel_opt:
    print(item.text)
