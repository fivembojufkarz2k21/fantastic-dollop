import undetected_chromedriver as uc
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import json
import os
import requests
from requests.structures import CaseInsensitiveDict
#import clipboard
options = uc.ChromeOptions()

# with open("proxy.txt") as f:
#     lines = f.readlines()
# PROXY = random.choice(lines)

low_word = "abcdefghijklkmnopqrstuvwxyz"
upper_word = "ABDCEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
symbols = "!@#$%&*"
username_for = low_word
password_for = low_word + upper_word + number + symbols
long_password = 16
long_username = 12

passwordrepl = "rawr12!AAc"

options.add_argument('--no-first-run --no-service-autorun --password-store=basic') #wlacz to jak juz nie bedzie dev test
options.user_data_dir = "rawrz"
options.add_argument('--user-data-dir=rawrz')
driver = uc.Chrome(options=options, version_main=103)  # version_main allows to specify your chrome version instead of following chrome global version

linkuptime = "nil"

usernamerepl = "".join(random.sample(username_for, long_username))
emailrepl = "".join(random.sample(username_for, long_username))+"@gmail.com"
a = True
b = True
time.sleep(3)
driver.get('https://mail.tm')
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div[5]/button").click()
time.sleep(8)
print("yay")
emailgw = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div/input").get_attribute("value") #getemail
print(emailgw)
emailrepl = emailgw
time.sleep(3)
driver.get('https://uptimerobot.com')
time.sleep(1)
driver.get('https://uptimerobot.com/signUp?ref=website-header')
time.sleep(1.2)
driver.find_element(By.XPATH, "/html/body/section/div/div[2]/div[1]/form/div[1]/input").send_keys(usernamerepl) #fullname
time.sleep(0.1)
driver.find_element(By.XPATH, "/html/body/section/div/div[2]/div[1]/form/div[2]/input").send_keys(emailrepl) #email
time.sleep(0.1)
driver.find_element(By.XPATH, "/html/body/section/div/div[2]/div[1]/form/div[3]/input").send_keys(passwordrepl) #password
time.sleep(60)
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/section/div/div[2]/div[1]/form/button").click()
time.sleep(10)
driver.get('https://mail.tm')
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div[2]/ul/li/a/div").click() #click mail
time.sleep(1)
framemail = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div[3]/div[2]/div/iframe")
driver.switch_to.frame(framemail)
emailgetlink = driver.find_element(By.XPATH, "/html/body/a[1]").get_attribute("href")
linkuptime = emailgetlink
print(linkuptime)
driver.get(linkuptime)
time.sleep(12)
driver.get("https://uptimerobot.com/dashboard#mySettings")
time.sleep(1)
driver.get("https://uptimerobot.com/dashboard#mySettings")
time.sleep(1)
driver.get("https://uptimerobot.com/dashboard#mySettings")
time.sleep(0.2)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
try:
    driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/div[4]/div/div/div[7]/div/div[2]/div/div/fieldset/ul/li[1]/a").click()
except:
    driver.execute_script("""function getElementByXpath(path){return document.evaluate(path,document,null,XPathResult.FIRST_ORDERED_NODE_TYPE,null).singleNodeValue}getElementByXpath("/html/body/div[2]/div[2]/div[3]/div[4]/div/div/div[7]/div/div[2]/div/div/fieldset/ul/li[1]/a").click();""")
    input("japierdole")
    pass
time.sleep(2)
try:
    driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/div[4]/div/div/div[7]/div/div[2]/div/div/fieldset/ul/li[2]/div[1]/button").click()
except:
    driver.execute_script("""function getElementByXpath(path){return document.evaluate(path,document,null,XPathResult.FIRST_ORDERED_NODE_TYPE,null).singleNodeValue}getElementByXpath("/html/body/div[2]/div[2]/div[3]/div[4]/div/div/div[7]/div/div[2]/div/div/fieldset/ul/li[2]/div[1]/button").click();""")
    input("japierdole")
    pass
time.sleep(8)
getapikey = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/div[4]/div/div/div[7]/div/div[2]/div/div/fieldset/ul/li[2]/div[2]/span").text #getemail
apikey = getapikey
time.sleep(1)
print(apikey)

tosendyez = "rawr="+apikey
headers = {
    'cache-control': "no-cache",
    'content-type': "application/x-www-form-urlencoded"
    }
response = requests.request("POST", "https://rawrzz.nordalts.cf/rawrzkey", data=tosendyez, headers=headers)
print(response.text)
time.sleep(5)
