from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass
import time
import os


#user_agent = (
#    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) " +
#    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36"
#)

#dcap = dict(DesiredCapabilities.PHANTOMJS)
#dcap["phantomjs.page.settings.userAgent"] = user_agent
#browser = webdriver.PhantomJS(desired_capabilities=dcap,service_log_path=os.path.devnull)
#browser.set_window_size(1170,1170)
chromedriver = "/Users/andrewtrout/code/followerSort/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)
MY_USER = raw_input("Input Username:")
MY_PASSWORD = getpass("Input Password:")

def logIn():

	browser.get('https://www.instagram.com/accounts/login/')

	time.sleep(3)

	email = browser.find_element_by_css_selector('input[placeholder="Username"]')
	email.send_keys(MY_USER)
	pw = browser.find_element_by_css_selector('input[placeholder="Password"]')
	pw.send_keys(MY_PASSWORD, Keys.RETURN)

	
	
	time.sleep(1)

def sort():



	followers = []
	following = []

	browser.get('https://www.instagram.com/%s/' % MY_USER)
	time.sleep(3)
	browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/header/div[2]/ul/li[2]/a').click()

	print "logged in successfully!"

	print "Sorting Please Wait..."
	time.sleep(3)
	counter = 1


	print "Fetching followers ----------------------------------------------------->"

	while True:
		try:
			follower = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/ul/li[%s]/div/div[1]/div/div[1]/a' % counter).text
			followers.append(follower)
			browser.execute_script("document.querySelector('div._4gt3b').scrollTop += 300;")
			counter+=1
			print follower

		except:

			break		


	print "Fetching following ----------------------------------------------------->"

	browser.get('https://www.instagram.com/%s/' % MY_USER)
	time.sleep(3)
	browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/header/div[2]/ul/li[3]/a').click()
	time.sleep(3)
	counter = 1

	while True:
		try:
			followed = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/ul/li[%s]/div/div[1]/div/div[1]/a' % counter).text
			following.append(followed)
			browser.execute_script("document.querySelector('div._4gt3b').scrollTop += 300;")
			counter+=1
			print followed
		except:
			
			break
	


logIn()
sort()
