from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

browser = webdriver.Chrome(executable_path = "E:\LT_Technology_Services\selenium\chromedriver.exe")
browser.get('http://automationpractice.com/index.php')
time.sleep(3)

login = browser.find_element_by_class_name("login")
login.click()

#First run the registration script commenting the Validation script and then check validation by commenting Registration
#Registration

email = browser.find_element_by_id("email_create")
email.send_keys("anup@gmail.com")

browser.find_element_by_id("SubmitCreate").click()
time.sleep(5)
radio_button = browser.find_element_by_id("id_gender1")
radio_button.click()

browser.find_element_by_id("customer_firstname").send_keys("Anup")
browser.find_element_by_id("customer_lastname").send_keys("Basumatary")
browser.find_element_by_id("passwd").send_keys("Anup123")

dropdown1 = browser.find_element_by_id("days")
dropdown_obj1 = Select(dropdown1)
dropdown_obj1.select_by_value("14")

dropdown2 = browser.find_element_by_id("months")
dropdown_obj2 = Select(dropdown2)
dropdown_obj2.select_by_value("2")

dropdown3 = browser.find_element_by_id("years")
dropdown_obj3 = Select(dropdown3)
dropdown_obj3.select_by_value("1990")

browser.find_element_by_id("optin").click()
browser.find_element_by_id("firstname").send_keys("Anup")
browser.find_element_by_id("lastname").send_keys("Basumatary")
browser.find_element_by_id("address1").send_keys("Napaam")
browser.find_element_by_id("city").send_keys("Udalguri")

dropdown_element = browser.find_element_by_id("id_state")
dropdown_object = Select(dropdown_element)
dropdown_object.select_by_value("9")

browser.find_element_by_id("postcode").send_keys("11044")
browser.find_element_by_id("phone").send_keys("9854687")
browser.find_element_by_id("phone_mobile").send_keys("7002811115")
browser.find_element_by_id("alias").send_keys("  India")

Register_button = browser.find_element_by_id("submitAccount").click()
time.sleep(5)

#VALIDATION

email = browser.find_element_by_id("email").send_keys("anup@gmail.com")
password = browser.find_element_by_id("passwd").send_keys("Anup123")
login = browser.find_element_by_id("SubmitLogin").click()

