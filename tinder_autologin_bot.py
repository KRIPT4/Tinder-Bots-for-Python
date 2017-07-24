#!/usr/bin/env python
"""
@name:tinder_autologin_bot.py - Tinder AutoLogin Bot
@disclaimer:Copyright 2017, KRIPT4
@lastrelease: Jul 23 2017 20:55
More info:
 * KRIPT4: https://github.com/KRIPT4/Tinder-Bots-for-Python
"""

# Import unittest module for creating unit tests
import unittest

# Import time module to implement 
import time

# Import win32com 
import win32com.client

# Import the Selenium 2 module (aka "webdriver")
from selenium import webdriver

# For automating data input
from selenium.webdriver.common.keys import Keys

# For providing custom configurations for Chrome to run
from selenium.webdriver.chrome.options import Options

start_time = time.time()		# TIME EXECUTION TEST

chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument("--enable-notifications")
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument('--enable-precise-memory-info')
chrome_options.add_argument('--ignore-ssl-errors=true --debug=true')
chrome_options.add_argument('--window-size=1100,1010') #Web Version
chrome_options.add_experimental_option('prefs', {
    'credentials_enable_service': False,
    'profile': {
        'password_manager_enabled': False
    }
})
chrome_options.add_experimental_option('prefs', {
    'geolocation': True
})
global driver

def mainExe():
	global driver
	varUSER = 'USER-FB'
	varPASS = 'PASS-FB'
	driver = webdriver.Chrome(executable_path = '?:\PATH\TO\chromedriver.exe', chrome_options = chrome_options)
	driver.get('https://www.tinder.com/app/login')
	time.sleep(1)
	window_before = driver.window_handles[0]
	## LOGIN
	retryElement('//*[@id="content"]/div/span/div/div[1]/div/aside/span/div/div/div/div[2]/div/div[3]/button').click()
	time.sleep(2)
	driver.switch_to_window(driver.window_handles[-1])
	retryElement('//*[@name = "email"]').send_keys(varUSER)
	retryElement('//*[@name = "pass"]').send_keys(varPASS)
	retryElement('//*[@name = "login"]').click()
	time.sleep(1)
	driver.switch_to_window(window_before)
	time.sleep(5)
	retryElement('//*[@id="content"]/div/span/div/div[2]/div[1]/div/div[1]/button').click()
	time.sleep(3)
	retryElement('//*[@id="content"]/div/span/div/div[2]/div[1]/div/div[2]/button').click()
	time.sleep(3)
	retryElement('//*[@id="content"]/div/span/div/div[2]/div[1]/div/div/div[1]/div/div[4]/button[1]').click()
	time.sleep(3)
	retryElement('//*[@id="content"]/div/span/div/div[2]/div[1]/div/div/div[1]/div/div[4]/button[2]').click()
	time.sleep(3)
	## END LOGIN

	elapsed_time = time.time() - start_time
	print("Elapsed time: %.10f seconds." % elapsed_time)

def retryElement(xpath):
	for i in range(0,50):
		try:
			element = driver.find_element_by_xpath(xpath)
			return element
		except Exception as e:
			time.sleep(0.1)
			continue
	brikear(("Error XPATH: %s" % xpath))

def brikear(msg):
	print(msg)
	closeDriver()
	sys.exit(1)

def closeDriver():
	global driver
	driver.quit()

try:
	mainExe()
except Exception as e:
	print(e)
	closeDriver()