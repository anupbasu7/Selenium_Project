from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome(executable_path = "E:\LT_Technology_Services\selenium\chromedriver.exe")
browser.get('http://automationpractice.com/index.php')
time.sleep(3)

login = browser.find_element_by_class_name("login")
login.click()

email = browser.find_element_by_id("email_create").send_keys("anup@gmail")
browser.find_element_by_id("SubmitCreate").click()

#Validation
error_message = browser.find_element_by_id("create_account_error").text
browser.execute_script("alert('Invalid Email Address');")
