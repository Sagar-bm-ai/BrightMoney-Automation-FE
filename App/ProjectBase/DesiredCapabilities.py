from appium import webdriver
'''
In this file modify capabilities like udid, platformName, platformVersion, deviceName
accordinng to your mobile device capability.

'''

def desiredCaps():

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
    return driver

# desiredCaps()
