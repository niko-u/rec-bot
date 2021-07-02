from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import time

driver = webdriver.Chrome()

driver.get("https://mycampusrec.tcu.edu")
driver.execute_script("showLogin('/')")
driver.implicitly_wait(10)
elem = driver.find_element_by_xpath('//*[@id="divLoginOptions"]/div[2]/div[2]/div/button')
driver.implicitly_wait(10)
elem.click()

#credentials
username = #username here
password = #passpord here

#tcu login

userfield = driver.find_element_by_xpath('//*[@id="okta-signin-username"]')
passfield = driver.find_element_by_xpath('//*[@id="okta-signin-password"]')
enterbutton = driver.find_element_by_xpath('//*[@id="okta-signin-submit"]')
userfield.send_keys(username)
passfield.send_keys(password)
enterbutton.click()

#rec website
reservations = driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div[1]/div[1]/a')
reservations.click()

#today
today = datetime.datetime.today().weekday()

#time slot (3pm)
if today == 4 or today == 5 or today == 6:
    weekendTimeSlot = driver.find_element_by_xpath('//*[@id="divBookingSlots"]/div/div[2]/div/button')
    weekendTimeSlot.click()
else:
    weekdayTimeSlot = driver.find_element_by_xpath('//*[@id="divBookingSlots"]/div/div[3]/div/button')
    weekdayTimeSlot.click()

driver.quit()

#crontab -e 0 10 * * * /usr/bin/python3 reservation.py
