from split import whitelist_user,change_split,delete_bright_uid_from_whitelist
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from FindBUID import get_bright_uid
from CheckingLink import linkCheckingAccount
import random

# 9211295590 is the number which ran through the automation and is at 

desired_caps={
    "udid": "PLEGAR1760905543",
  "platformName": "Android",
  "platformVersion": "9",
  "deviceName": "Nokia 6",
  "automationName": "UiAutomator2",
  "appPackage": "com.brightcapital.app.dev",
  "appActivity": "com.brightcapital.app.MainActivity"
}

driver= webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

wait =WebDriverWait(driver,50)
phone='9211296646'
change_split("on")
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,'//android.widget.Button')))
# driver.implicitly_wait(20)
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

# try:
#   action=ActionChains(driver)
#   action.send_keys('1').perform()
#   action.send_keys('2').perform()
#   action.send_keys('3').perform()
#   action.send_keys('4').perform()
#   action.send_keys('5').perform()
#   action.send_keys('6').perform()
# except:
#   print('action for verification has failed')

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Firebase user lost! Ignore']")))
driver.find_element_by_xpath("//android.widget.Button[@text='GOT IT']").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Set a Pin Code']")))

# try:
#   act=ActionChains(driver)
#   act.send_keys('1').perform()
#   act.send_keys('1').perform()
#   act.send_keys('1').perform()
#   act.send_keys('1').perform()
# except:
#   print('action for pin has failed')

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Re-enter the Pin Code']")))

# try:
#   ac=ActionChains(driver)
#   ac.send_keys('1').perform()
#   ac.send_keys('1').perform()
#   ac.send_keys('1').perform()
#   ac.send_keys('1').perform()
# except:
#   print('action for re-enter has failed')

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Would you like to turn on Fingerprint?']")))
driver.find_element_by_xpath("//android.widget.Button[@text='CANCEL']").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.EditText[@content-desc='txt_FirstName']")))
driver.find_element_by_accessibility_id('txt_FirstName').send_keys("Sagar")
driver.find_element_by_accessibility_id('txt_LastName').send_keys("Sharma")
driver.find_element_by_accessibility_id('btn_Continue').click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.EditText[@content-desc='txt_EmailID']")))
r=random.randint(1001,99999999)
driver.find_element_by_accessibility_id('txt_EmailID').send_keys("sagarSharmaAutomation"+str(r)+"@brightmonneyy.co")
driver.find_element_by_accessibility_id('btn_Save').click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Tell us a bit about yourself so we can verify your account']")))
driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys('0')
driver.find_element_by_xpath("//android.widget.EditText[@index='1']").send_keys('8')
driver.find_element_by_xpath("//android.widget.EditText[@index='3']").send_keys('2')
driver.find_element_by_xpath("//android.widget.EditText[@index='4']").send_keys('7')
driver.find_element_by_xpath("//android.widget.EditText[@index='6']").send_keys('1')
driver.find_element_by_xpath("//android.widget.EditText[@index='7']").send_keys('9')
driver.find_element_by_xpath("//android.widget.EditText[@index='8']").send_keys('8')
driver.find_element_by_xpath("//android.widget.EditText[@index='9']").send_keys('0')
driver.find_element_by_accessibility_id('btn_Continue').click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Where do you live?']")))
driver.find_element_by_accessibility_id('txt_Address').send_keys('1500 15th')
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='1600 15th Street, San Francisco, CA, USA']")))
driver.find_element_by_accessibility_id('addr-0').click()

bright_uid = get_bright_uid("+1"+phone)
whitelist_user("target_card_in_funnel_experiment",bright_uid,"off")

driver.implicitly_wait(5)
driver.find_element_by_accessibility_id('btn_Continue').click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Great! Now, let’s work on YOUR tailored debt-free plan']")))
driver.find_element_by_accessibility_id('btn_Next').click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Connect your bank account']")))
driver.find_element_by_accessibility_id('btn_Connect_Bank_Acc').click()

linkCheckingAccount('+1'+phone)

# driver.quit()

# driver= webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

driver.reset()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,'//android.widget.Button')))
# driver.implicitly_wait(20)
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
driver.find_element_by_xpath("//android.widget.TextView[@text='Login']").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.EditText[@content-desc='txt_PhoneNo_Login']")))
driver.find_element_by_accessibility_id('txt_PhoneNo_Login').click()
driver.find_element_by_accessibility_id('txt_PhoneNo_Login').send_keys(phone)
driver.find_element_by_accessibility_id('btn_Continue_Login').click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@content-desc='lbl_Verification_text']")))

# try:
#   action=ActionChains(driver)
#   action.send_keys('1').perform()
#   action.send_keys('2').perform()
#   action.send_keys('3').perform()
#   action.send_keys('4').perform()
#   action.send_keys('5').perform()
#   action.send_keys('6').perform()
# except:
#   print('action for verification has failed')

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Firebase user lost! Ignore']")))
driver.find_element_by_xpath("//android.widget.Button[@text='GOT IT']").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Set a Pin Code']")))

# try:
#   act=ActionChains(driver)
#   act.send_keys('1').perform()
#   act.send_keys('1').perform()
#   act.send_keys('1').perform()
#   act.send_keys('1').perform()
# except:
#   print('action for pin has failed')

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Re-enter the Pin Code']")))

# try:
#   ac=ActionChains(driver)
#   ac.send_keys('1').perform()
#   ac.send_keys('1').perform()
#   ac.send_keys('1').perform()
#   ac.send_keys('1').perform()
# except:
#   print('action for re-enter has failed')

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Would you like to turn on Fingerprint?']")))
driver.find_element_by_xpath("//android.widget.Button[@text='CANCEL']").click()


wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@content-desc='lbl_SelectCheckingAccount']")))
driver.find_element_by_accessibility_id("card-0000").click()
driver.implicitly_wait(2)
driver.find_element_by_accessibility_id("btn_Continue").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[contains(@text,'US regulations')]")))
driver.find_element_by_xpath("//android.widget.EditText").send_keys("643672054")
driver.implicitly_wait(3)
driver.find_element_by_accessibility_id("btn_Continue").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@content-desc='lbl_Howmuchpay']")))
driver.find_element_by_accessibility_id("txt_Amount").send_keys('999')
driver.implicitly_wait(3)
driver.find_element_by_xpath("//android.widget.Button").click()


wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='It all starts with a good plan']")))
driver.implicitly_wait(3)
driver.find_element_by_accessibility_id("btn_GotIt").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='What types of debts do you currently have?']")))
driver.find_element_by_xpath("//android.widget.TextView[@text='Credit Card Debt']").click()
driver.find_element_by_accessibility_id("btn_Next").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='How much total credit card debt do you currently have?']")))
driver.find_element_by_xpath("//android.widget.TextView[@text='Less than $500']").click()
driver.find_element_by_accessibility_id("btn_Next").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='What is the balance of the card you’d want to pay off first?']")))
driver.find_element_by_xpath("//android.widget.TextView[@text='Less than $500']").click()
driver.find_element_by_accessibility_id("btn_Next").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@content-desc='brightPlan_Title']")))
driver.implicitly_wait(3)
driver.find_element_by_accessibility_id("next_button").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.Button[@content-desc='Moderate']")))
driver.find_element_by_accessibility_id("Moderate").click()
driver.implicitly_wait(3)
driver.find_element_by_accessibility_id("next_button").click()

# monetization screen
driver.find_element_by_xpath("//android.widget.Button").click()


wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Congratulations Sagar!']")))
driver.find_element_by_xpath("//android.widget.Button").click()

# d14 begin
delete_bright_uid_from_whitelist("target_card_in_funnel_experiment",bright_uid,"off")












