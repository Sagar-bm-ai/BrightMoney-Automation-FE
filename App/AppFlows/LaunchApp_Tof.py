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


driver = desiredCaps()
wait = WebDriverWait(driver,50)

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.TextView[@text='Get Started']")))
driver.find_element_by_xpath("//android.widget.TextView[@text='Login']").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//android.widget.Button[@content-desc='btn_Next']")))
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
top_goal_options[N].click()



