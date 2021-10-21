from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from FindBUID import get_bright_uid
from CheckingLink import linkCheckingAccount
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ProjectBase.DesiredCapabilities import desiredCaps
import random
import time

phone = '1288218829'
driver = desiredCaps()
wait = WebDriverWait(driver,50)

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Get Started']")))
driver.find_element_by_xpath("//android.widget.TextView[@text='Login']").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.Button[@content-desc='btn_Next']")))
driver.find_element_by_xpath("(//android.view.ViewGroup)[10]").click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("(//android.view.ViewGroup)[10]").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.Button[@content-desc='option-0']")))
driver.find_element_by_xpath("//android.widget.Button[@content-desc='option-0']").click()
driver.find_element_by_xpath("//android.widget.TextView[@text='Continue']").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='update installed']")))
driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Pay off credit cards']")))
top_goal_options = [driver.find_element_by_xpath("//android.widget.TextView[@text='Pay off credit cards']"),driver.find_element_by_xpath("//android.widget.TextView[@text='Own a home']"),driver.find_element_by_xpath("//android.widget.TextView[@text='Build savings']"),driver.find_element_by_xpath("//android.widget.TextView[@text='Improve credit score']")]
N = random.randint(0,3)
chosen_goal = top_goal_options[N].text
print(chosen_goal)
top_goal_options[N].click()
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[contains(@text,'Congratulations')]")))
driver.find_element_by_xpath("//android.widget.Button").click()
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Built by the best']")))
driver.find_element_by_xpath("//android.widget.Button").click()
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@content-desc='lbl_WhatImportant']")))
driver.find_element_by_xpath("(//android.view.ViewGroup)[10]").click()
driver.implicitly_wait(3)
driver.find_element_by_accessibility_id('btn_Next').click()
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='One step closer to debt-free']")))
driver.find_element_by_xpath("//android.widget.Button").click()
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@content-desc='lbl_WhatImportant']")))
driver.find_element_by_xpath("(//android.view.ViewGroup)[10]")
driver.implicitly_wait(3)
driver.find_element_by_accessibility_id('btn_Next').click()
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"(//android.widget.Button[@content-desc='btn_Next'])[2]")))
driver.find_element_by_xpath("(//android.widget.Button[@content-desc='btn_Next'])[2]").click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("(//android.view.ViewGroup)[10]").click()
driver.implicitly_wait(20)
driver.find_element_by_accessibility_id('btn_Next').click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("(//android.view.ViewGroup)[10]").click()
driver.find_element_by_accessibility_id("btn_Next").click()
# wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Done! Your Bright Plan is ready']")))
# driver.find_element_by_accessibility_id('btn_Next').click()
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Join 1,000s of members achieving financial well-being']")))
driver.find_element_by_xpath("//android.widget.Button").click()
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@content-desc='lbl_PhoneNo_Login']")))

driver.find_element_by_xpath("//android.widget.EditText").send_keys(phone)
driver.find_element_by_accessibility_id('btn_Next').click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@content-desc='lbl_SentCode_CodeVerify']")))
driver.implicitly_wait(3)
ActionChains(driver).send_keys('111111').perform()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Firebase user lost! Ignore']")))
driver.find_element_by_xpath("//android.widget.Button[@text='GOT IT']").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Set a Pin Code']")))
ActionChains(driver).send_keys('1111').perform()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Re-enter the Pin Code']")))
ActionChains(driver).send_keys('1111').perform()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Would you like to turn on Fingerprint?']")))
driver.find_element_by_xpath("//android.widget.Button[@text='CANCEL']").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='See my plan outline']")))
driver.find_element_by_xpath("//android.widget.Button").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@content-desc='brightPlan_Title']")))
driver.find_element_by_accessibility_id("next_button").click()


wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Let’s start with some basic information']")))
driver.find_element_by_xpath("(//android.widget.EditText)[1]").click()
driver.find_element_by_xpath("(//android.widget.EditText)[1]").send_keys('Alexander')

driver.find_element_by_xpath("(//android.widget.EditText)[2]").click()
driver.find_element_by_xpath("(//android.widget.EditText)[2]").send_keys('Seyfert')

driver.find_element_by_accessibility_id("btn_Next").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='What’s your email address?']")))
num = random.randint(10000,100000)
driver.find_element_by_xpath("//android.widget.EditText").send_keys("alexisTesting+Automation"+str(num)+"@brightmoney.co")
driver.implicitly_wait(3)
driver.find_element_by_accessibility_id("btn_Next").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='When were you born?']")))
driver.find_element_by_xpath("(//android.widget.EditText)[1]").send_keys('0')
driver.find_element_by_xpath("(//android.widget.EditText)[2]").send_keys('9')
driver.find_element_by_xpath("(//android.widget.EditText)[3]").send_keys('2')
driver.find_element_by_xpath("(//android.widget.EditText)[4]").send_keys('7')
driver.find_element_by_xpath("(//android.widget.EditText)[5]").send_keys('1')
driver.find_element_by_xpath("(//android.widget.EditText)[6]").send_keys('9')
driver.find_element_by_xpath("(//android.widget.EditText)[7]").send_keys('8')
driver.find_element_by_xpath("(//android.widget.EditText)[8]").send_keys('0')

driver.implicitly_wait(2)
driver.find_element_by_xpath("//android.widget.Button").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Where do you live?']")))
driver.find_element_by_xpath("//android.widget.EditText").send_keys("1600 15th")
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='1600 15th Street, San Francisco, CA, USA']")))
driver.find_element_by_xpath("//android.widget.TextView[@text='1600 15th Street, San Francisco, CA, USA']").click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("//android.widget.TextView[@text='1600 15th Street, San Francisco, CA, USA']").click()
driver.implicitly_wait(3)
driver.find_element_by_accessibility_id("btn_Next").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Connect your account to personalize your plan']")))
driver.find_element_by_accessibility_id('btn_Connect_Bank_Acc').click()

driver.implicitly_wait(20)
linkCheckingAccount("+1"+phone)

driver.terminate_app('com.brightcapital.app.dev')
driver.activate_app('com.brightcapital.app.dev')

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Enter PIN']")))
ActionChains(driver).send_keys('1111').perform()
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Firebase user lost! Ignore']")))
driver.find_element_by_xpath("//android.widget.Button[@text='GOT IT']").click()

# select checking , ssn, pay amt, 
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@content-desc='lbl_WhatImportant']")))
driver.find_element_by_accessibility_id('btn_Continue')

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='To comply with regulations, we need to verify your identity one more time.']")))
driver.find_element_by_xpath("//android.widget.EditText").send_keys("643672054")
driver.find_element_by_xpath("//android.widget.Button").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='How much do you pay?']")))
driver.find_element_by_accessibility_id("txt_Amount").send_keys(999)
driver.find_element_by_xpath("//android.widget.Button").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Your future is about to get a lot Brighter.']")))
driver.find_elements_by_accessibility_id("btn_Next").send_keys(999)

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@content-desc='brightPlan_Title']")))
driver.find_elements_by_accessibility_id("next_button").click()

ActionChains(driver).click(driver.find_elements_by_accessibility_id("step2Title")).perform()
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.Button[@content-desc='Moderate']")))
driver.find_elements_by_accessibility_id("Moderate").click()
driver.find_element_by_xpath("//android.widget.TextView[@text='Continue']").click()

driver.implicitly_wait(5)
driver.find_element_by_xpath("//android.widget.TextView[@text='Continue']").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@content-desc='focusCardTitle']")))
driver.find_elements_by_accessibility_id("next_button").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.view.ViewGroup[@content-desc='tgl_Autofill']")))
driver.find_element_by_xpath("//android.widget.TextView[@text='Continue']").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.view.ViewGroup[@content-desc='brightRecommendTitle']")))
driver.find_element_by_xpath("//android.widget.TextView[@text='Continue']").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.Button[@content-desc='btn_Skip']")))
driver.find_elements_by_xpath("//android.widget.EditText").send_keys("4617123412353333")
driver.find_element_by_xpath("//android.widget.TextView[@text='Continue']").click()











