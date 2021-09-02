from webdriver_manager.chrome import ChromeDriverManager
# import webdriver
from selenium import webdriver

# import Action chains
from selenium.webdriver.common.action_chains import ActionChains

# create webdriver object
driver = webdriver.Chrome(ChromeDriverManager().install())

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# get element
driver.find_element_by_class_name("gcse-search__btn").click()
element = driver.find_element_by_class_name("gcse-search-input__wrapper")

# create action chain object
action = ActionChains(driver)

# click the item
action.click(on_element = element)

# send keys
action.send_keys("Arrays")

# perform the operation
action.perform()
driver.quit()

