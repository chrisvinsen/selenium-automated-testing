from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

def slow_typing(element, text):
   for character in text: 
      element.send_keys(character)
      time.sleep(0.1)

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.get("https://tiket.com")

place_from = "Jakarta"
place_to = "Medan"
fullname = "Name Name"
email = "tester1239@gmail.com"
phone = "081234567890"

flight_type = driver.find_element_by_id("oneWay")
driver.execute_script("arguments[0].click();", flight_type)

input_from = driver.find_element_by_id("productSearchFrom")
input_from.clear()
slow_typing(input_from, place_from)
time.sleep(1)
input_from.send_keys(Keys.ENTER)

input_to = driver.find_element_by_id("productSearchTo")
input_to.clear()
slow_typing(input_to, place_to)
time.sleep(1)
input_to.send_keys(Keys.ENTER)

driver.find_element_by_class_name("product-form-search-btn").send_keys(Keys.ENTER)

driver.find_element_by_class_name("btn-action").click()
time.sleep(2)

driver.find_elements_by_class_name("btn-book-now")[-1].click()
time.sleep(2)

driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[1]/div[3]/div[1]/div[1]/div/input").click()
time.sleep(1)
driver.find_element_by_xpath("//body/div[@id='app']/div[1]/div[3]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/ul[1]/li[1]").click()

input_fullname = driver.find_element_by_xpath("//body/div[@id='app']/div[1]/div[3]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/input[1]")
slow_typing(input_fullname, fullname)

input_email = driver.find_element_by_xpath("//body/div[@id='app']/div[1]/div[3]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/input[1]")
slow_typing(input_email, email)

input_phone = driver.find_element_by_xpath("//body/div[@id='app']/div[1]/div[3]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[3]/div[2]/div[1]/input[1]")
slow_typing(input_phone, phone)

driver.find_element_by_xpath("//body/div[@id='app']/div[1]/div[3]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/label[1]").click()

driver.find_element_by_xpath("//button[contains(text(),'LANJUTKAN KE PEMBAYARAN')]").click()
time.sleep(1)

driver.find_element_by_xpath("//button[contains(text(),'YA, LANJUTKAN')]").click()