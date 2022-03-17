from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

browser = webdriver.Chrome(executable_path = "E:\LT_Technology_Services\selenium\chromedriver.exe")
browser.get('http://automationpractice.com/index.php')
time.sleep(3)

login = browser.find_element_by_class_name("login")
login.click()

email = browser.find_element_by_id("email_create")
email.send_keys("anupxyz@gmail.com")

browser.find_element_by_id("SubmitCreate").click()
time.sleep(5)

browser.find_element_by_id("customer_firstname").send_keys("1234")
browser.find_element_by_id("customer_lastname").send_keys("9876")
browser.find_element_by_id("passwd").send_keys("Anup123")

browser.find_element_by_id("address1").send_keys("0000")
browser.find_element_by_id("city").send_keys("1111")

dropdown_element = browser.find_element_by_id("id_state")
dropdown_object = Select(dropdown_element)
dropdown_object.select_by_value("9")

browser.find_element_by_id("postcode").send_keys("abc")
browser.find_element_by_id("phone").send_keys("xyz")
browser.find_element_by_id("phone_mobile").send_keys("qwerty")
browser.find_element_by_id("alias").send_keys("India")

Register_button = browser.find_element_by_id("submitAccount").click()
time.sleep(3)

error_message = browser.find_element_by_xpath('//*[@id="center_column"]/div').text
print(error_message)