##################################################################################################################################################################
#Written by Brandon Ruggles (brandonrninefive@gmail.com) :)
##################################################################################################################################################################

import json
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

confFile = None
orders = []
debug = True

try:
	#We read our JSON data from a file called 'checkout.conf' for simplicity and readability.
	confFile = open("checkout.conf")
	orders = json.loads(confFile.read())["orders"]
except Exception as e:
	print "Error: either no checkout.conf was found, or it contains invalid JSON syntax!"
	if(debug):
		print 'Error Details: ' + str(e)
	
def login(username, password):
	if(username != '' and password != ''):
		driver.get('http://www.nakedcph.com/login')
		usernameBox = driver.find_element_by_xpath('/html/body/div[@id="main"]/div[@id="main-content"]/div/form/ul/li[@id="login-form-li-email"]/input')
		passwordBox = driver.find_element_by_xpath('/html/body/div[@id="main"]/div[@id="main-content"]/div/form/ul/li[@id="login-form-li-password"]/input')
		usernameBox.send_keys(username)
		passwordBox.send_keys(password)
		passwordBox.send_keys(Keys.ENTER)
		return True
	return False

def autoCompleteCaptcha():
	try:
		captchaBox = driver.find_element_by_xpath('/html/body/div[@id="main"]/div[@id="main-content"]/div/div[@id="commodity-show-right"]/div/form/ul/li/input[@id="commodity-show-security-code"]')
		code = raw_input('A Captcha box has been detected! Please type in the Captcha code displayed: ')
		captchaBox.send_keys(code)
		captchaBox.send_keys(Keys.ENTER)
		print 'Attempting to continue with entered Captcha code...'
	except Exception as e:
		print 'No Captcha box detected! Proceeding with the item.'
		if(debug):
			print 'Error Details: ' + str(e)
	
def addToCart(product):
		driver.get(product['url'])
		autoCompleteCaptcha()
		sizeSelection = driver.find_element_by_xpath('/html/body/div[@id="main"]/div[@id="main-content"]/div/div[@id="commodity-show-right"]/div/form/select[@id="commodity-show-form-size"]/option[text()="'+ product['size']  + '"]')
		sizeSelection.click()
		addButton = driver.find_element_by_xpath('/html/body/div[@id="main"]/div[@id="main-content"]/div/div[@id="commodity-show-right"]/div/a')
		addButton.click()

def checkout(card_number, card_expiration, card_crn):
	cartButton = driver.find_element_by_xpath('/html/body/div[@id="header-container"]/div/div[@id="main-cart"]/a')
	cartButton.click()
	proceedButton = driver.find_element_by_xpath('/html/body/div[@id="main"]/div[@id="main-content"]/div/a[2]')
	proceedButton.click()
	emailBox = driver.find_element_by_xpath('/html/body/div[@id="main"]/div[@id="main-content"]/div/form/ul/li[@id="details-form-li-email"]/input')
	emailBox2 = driver.find_element_by_xpath('/html/body/div[@id="main"]/div[@id="main-content"]/div/form/ul/li[@id="details-form-li-email_repeat"]/input')
	checkoutButton = driver.find_element_by_xpath('/html/body/div[@id="main"]/div[@id="main-content"]/div/form/ul/li[15]/input[@id="details-form-submit"]')
	
	#We can take some shortcuts since we're logged in...
	emailBox2.send_keys(emailBox.get_attribute('value'))

	checkoutButton.click()
	checkoutButton2 = driver.find_element_by_xpath('/html/body/div[@id="main"]/div[@id="main-content"]/div/form/ul/li[3]/input[@id="handling-form-submit"]')
	checkoutButton2.click()
	
	totalTableBody = driver.find_element_by_xpath('/html/body/div[@id="main"]/div[@id="main-content"]/div/table/tbody')
	tableItems = totalTableBody.find_elements_by_xpath('/tr')	
	totalTableFooter = driver.find_element_by_xpath('/html/body/div[@id="main"]/div[@id="main-content"]/div/table/tfoot')
	tableTotalsItems = totalTableFooter.find_elements_by_xpath('/tr')
	print 'Checkout page details: '
	print ''
	for item in tableItems:
		tableItemDetails = item.find_elements_by_xpath('//td')
		printableDetails = ""
		print 'Item:'
		for detail in tableItemDetails:
			printableDetails += detail.text + ","
		print printableDetails
		print ''
	print 'Totals: '
	print ''
	for item in tableTotalsItems:
		tableTotalsItemName = item.find_element_by_xpath('//td[@class="title"]')
		tableTotalsItemValue = item.find_element_by_xpath('//td[@class="total"]')
		print tableTotalsItemName.text + ':' + tableTotalsItemValue.text
		print ''
	
	agreeBox = driver.find_element_by_xpath('/html/body/div[@id="main"]/div[@id="main-content"]/div/form/ul/li[@id="confirm-form-li-confirmed"]/input')

	agreeBox.click()

	checkoutButton3 = driver.find_element_by_xpath('/html/body/div[@id="main"]/div[@id="main-content"]/div/form/ul/li[2]/input[2]')
	
	checkoutButton3.click()

	cardBox = driver.find_element_by_xpath('/html/body/div/div[@id="content"]/div[@id="payment_details"]/form/dl/dd[1]/input')
	monthBox = driver.find_element_by_xpath('/html/body/div/div[@id="content"]/div[@id="payment_details"]/form/dl/dd[2]/input[1]')
	yearBox = driver.find_element_by_xpath('/html/body/div/div[@id="content"]/div[@id="payment_details"]/form/dl/dd[2]/input[2]')
	crnBox = driver.find_element_by_xpath('/html/body/div/div[@id="content"]/div[@id="payment_details"]/form/dl/dd[3]/input')
	completeButton = driver.find_element_by_xpath('/html/body/div/div[@id="content"]/div[@id="payment_details"]/form/input[2]')
	cardBox.send_keys(card_number)
	monthBox.send_keys(card_expiration[0:2])
	yearBox.send_keys(card_expiration[3:])
	crnBox.send_keys(card_crn)
	wait = WebDriverWait(driver, 30) #We keep trying to click the final button for 30 seconds before throwing an error
	completeButton = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[@id="content"]/div[@id="payment_details"]/form/input[2]')))
	completeButton.click()
	print 'Successfully clicked the order submit button. Please check the browser window to make sure that the order was checked out.'
	print ''

orderIndex = 1
for order in orders:
	print 'Processing order number ' + str(orderIndex) + '...'
	print ''
	driver = webdriver.Chrome()
	logged_in = login(order['username'], order['password'])
	if(logged_in):
		for product in order['products']:
			try:
				for i in range(product['quantity']):
					addToCart(product)
			except Exception as e:
				print "Error adding product to cart! Attempting to proceed anyway. Product URL: " + product["url"]
				if(debug):
					print 'Error Details: ' + str(e)
		try:
			checkout(order['credit_card_number'],order['credit_card_expiration'], order['credit_card_crn'])	
		except Exception as e:
			print "Error occured while checking out the order! Check the browser to see what went wrong. If the checkout page is missing certain credentials, you may have input an incorrect username/password combination. It is also possible that you tried to purchase too many of a particular item."
			if(debug):
				print 'Error Details: ' + str(e)
	else:
		print 'No username and/or password provided. The order cannot be processed.'
	orderIndex+=1

