from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
url = 'https://www.seleniumeasy.com/test/basic-first-form-demo.html'
driver.get(url)
messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys('Hello World')
showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButton.click()
print(driver.title)

a_value = driver.find_element_by_xpath('//*[@id="sum1"]')
b_value = driver.find_element_by_xpath('//*[@id="sum2"]')
a_value.send_keys(10)
b_value.send_keys(11)
get_total = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
get_total.click()
#driver.implicitly_wait(100)
driver.close()