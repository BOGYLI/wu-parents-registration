from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import argparse

argParser = argparse.ArgumentParser()
argParser.add_argument("-s", "--schoolurl", help="URL of your schools login page. E.g. \"nessa.webuntis.com/WebUntis/?school=bodenseegym-lindau\"")
argParser.add_argument("-m", "--mails", help="Path to the txt file including parents email addresses.")
args = argParser.parse_args()
import time

file = open(args.mails, "r")
for mail in file:

    driver = webdriver.Chrome()
    driver.get("https://"+args.schoolurl+"/WebUntis/#/basic/userRegistration")
    emailfield = driver.find_element(By.CSS_SELECTOR, "input.un-input-group__input")
    emailfield.send_keys(mail)
    emailfield.send_keys(Keys.RETURN)

    time.sleep(2)
    
    driver.close()

file.close()