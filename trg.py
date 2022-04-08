# this is script for register site nabegheha.com
# author : sadegh shadanpour from iran
# file's = *chrome* driver


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

driver = webdriver.Chrome()

driver.get('https://www.nabegheha.com')

time.sleep(3)

account = driver.find_element_by_xpath("/html/body/div[2]/header/div/div[1]/div[2]/ul/li[3]/a")

account.click()

time.sleep(2)

driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[1]/form/div[7]').click()

time.sleep(1)

entermail = input("Enter Your Email : ")

driver.find_element_by_xpath('//input[@name="digits_reg_mail"]').send_keys(f'{entermail}')

time.sleep(2)

enterpass = input("Enter Your Password : ")

driver.find_element_by_xpath('//input[@name="digits_reg_password"]').send_keys(f'{enterpass}')

time.sleep(3)

capt = input("Enter Captcha : ")

driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/form/div[1]/div[1]/div[3]/div/div/input').send_keys(f'{capt}')

time.sleep(2)

numbersum = input("Enter sum number : ")

driver.find_element_by_xpath("//input[@name='aiowps-captcha-answer']").send_keys(f'{numbersum}')

time.sleep(3)

registerdone = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/form/button')

registerdone.click()