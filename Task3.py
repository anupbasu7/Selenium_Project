from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome(executable_path = "E:\LT_Technology_Services\selenium\chromedriver.exe")
browser.get('http://automationpractice.com/index.php')
time.sleep(3)

login = browser.find_element_by_class_name("login")
login.click()

email = browser.find_element_by_id("email_create")
email.send_keys("anupxyz@gmail.com")

browser.find_element_by_id("SubmitCreate").click()
time.sleep(3)

Register_button = browser.find_element_by_id("submitAccount").click()
time.sleep(3)


error_message = browser.find_element_by_xpath('//*[@id="center_column"]/div').text
print(error_message)


