from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
desired_cap = {
    # Set your access credentials
    "browserstack.user" : "ankurvarshney1",
    "browserstack.key" : "y9vZE3c93WiKedpkSzwE",
    # Set URL of the application under test
    "app" : "bs://ecc57690c99acda0e547205687f038755dc4d0cd",
    # Specify device and os_version for testing
    "device" : "Google Pixel 3",
    "os_version" : "9.0",
    # Set other BrowserStack capabilities
    "project" : "Update app on browser stack",
    "build" : "Python Android",
    "name" : "first_test"
}
# Initialize the remote Webdriver using BrowserStack remote URL
# and desired capabilities defined above
driver = webdriver.Remote(
    command_executor="http://hub-cloud.browserstack.com/wd/hub",
    desired_capabilities=desired_cap
)
# Write your custom code here
phone = "1288211120"
wait =WebDriverWait(driver,50)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,'//android.widget.Button')))
driver.find_element_by_xpath("//android.widget.TextView[@text='Login']").click()
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.Button[@content-desc='btn_Continue_Login']")))
driver.find_element_by_xpath("//android.view.ViewGroup[@content-desc='btn_Back']").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.Button[@content-desc='option-0']")))
driver.find_element_by_xpath("//android.widget.Button[@content-desc='option-0']").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//android.widget.TextView[@text='Continue']").click()
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='update installed']")))
driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Get Started']")))
driver.find_element_by_xpath("//android.widget.TextView[@text='Get Started']").click()

driver.implicitly_wait(5)
driver.find_element_by_xpath("//android.widget.TextView[@text='Continue']").click()

driver.implicitly_wait(5)
driver.find_element_by_xpath("//android.widget.TextView[@text='Continue']").click()

driver.implicitly_wait(5)
driver.find_element_by_xpath("//android.widget.TextView[@text='Continue']").click()

driver.implicitly_wait(5)
driver.find_element_by_xpath("//android.widget.TextView[@text='Learn more']").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Built by the best']")))
driver.find_element_by_xpath("//android.widget.TextView[@text='Learn more']").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Boost your credit score!']")))
driver.find_element_by_xpath("//android.widget.TextView[@text='Continue']").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Yes, let’s do this...']")))
driver.find_element_by_xpath("//android.widget.TextView[@text='Yes, let’s do this...']").click()

driver.implicitly_wait(5)
driver.find_element_by_xpath("(//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup)[1]").click()
driver.find_element_by_accessibility_id('btn_Next').click()

driver.implicitly_wait(5)
driver.find_element_by_xpath("(//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup)[1]").click()
driver.find_element_by_accessibility_id('btn_Next').click()

driver.implicitly_wait(5)
driver.find_element_by_xpath("(//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup)[1]").click()
driver.find_element_by_accessibility_id('btn_Next').click()

driver.implicitly_wait(5)
driver.find_element_by_xpath("(//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup)[1]").click()
driver.find_element_by_accessibility_id('btn_Next').click()

driver.implicitly_wait(5)
driver.find_element_by_xpath("(//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup)[1]").click()
driver.find_element_by_accessibility_id('btn_Next').click()

driver.implicitly_wait(5)
driver.find_element_by_xpath("(//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup)[1]").click()
driver.find_element_by_accessibility_id('btn_Next').click()

driver.implicitly_wait(5)
driver.find_element_by_xpath("(//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup)[1]").click()
driver.find_element_by_accessibility_id('btn_Next').click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Your results are ready!']")))
driver.find_element_by_accessibility_id('btn_Next').click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.EditText[@content-desc='txt_PhoneNo_Login']")))
driver.find_element_by_accessibility_id('txt_PhoneNo_Login').click()
driver.find_element_by_accessibility_id('txt_PhoneNo_Login').send_keys(phone)
driver.find_element_by_accessibility_id('btn_Continue_Login').click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@content-desc='lbl_Verification_text']")))
element = driver.find_element_by_xpath("(//android.view.ViewGroup)[11]")
action=ActionChains(driver)
action.click(on_element = element)
action.send_keys("1")
action.perform()
time.sleep(2)
action.send_keys("1")
action.perform()
time.sleep(2)
action.send_keys("1")
action.perform()
time.sleep(2)
action.send_keys("1")
action.perform()
time.sleep(2)
action.send_keys("1")
action.perform()
time.sleep(2)
action.send_keys("1")
action.perform()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Firebase user lost! Ignore']")))


# Invoke driver.quit() after the test is done to indicate that the test is completed.
driver.quit()