import undetected_chromedriver as uc
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.webdriver.common.by import By
import json
import os
import requests
from requests.structures import CaseInsensitiveDict
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
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
options.user_data_dir = "rawr"
caps = DesiredCapabilities().CHROME
# caps["pageLoadStrategy"] = "normal"  #  Waits for full page load
caps["pageLoadStrategy"] = "none"   # Do not wait for full page load
options.add_argument('--user-data-dir=rawr')
driver = uc.Chrome(options=options, desired_capabilities=caps, version_main=102)  # version_main allows to specify your chrome version instead of following chrome global version
driver.get("https://client.falixnodes.net/auth/register")
time.sleep(10)
emailrepl = "".join(random.sample(username_for, long_username))+"@cldkid.com"
xd = False
frime = driver.find_element(By.XPATH, "/html/body/main/div/div/div/div/div/div/div[2]/div/form/center/div/iframe")
driver.switch_to.frame(frime)
timez = int(time.time())+300
while xd == False:
    time.sleep(1)
    print(driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div/div/div[1]").get_attribute("aria-checked"))
    if(timez<int(time.time())):
        cockz
    if(driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div/div/div[1]").get_attribute("aria-checked")=="false"):
        xd = False
    else:
        xd = True
driver.switch_to.default_content()
time.sleep(0.5)
driver.find_element(By.XPATH, "/html/body/main/div/div/div/div/div/div/div[2]/div/form/div[1]/input").send_keys(emailrepl)
time.sleep(0.1)
driver.find_element(By.XPATH, "/html/body/main/div/div/div/div/div/div/div[2]/div/form/div[2]/div[1]/input").send_keys("Cloudkid12!")
time.sleep(0.1)
driver.find_element(By.XPATH, "/html/body/main/div/div/div/div/div/div/div[2]/div/form/div[2]/div[2]/input").send_keys("Cloudkid12!")
driver.find_element(By.XPATH, "/html/body/main/div/div/div/div/div/div/div[2]/div/form/div[3]/input").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/main/div/div/div/div/div/div/div[2]/div/form/div[4]/button").click()
time.sleep(20)
driver.get("https://client.falixnodes.net/create")
time.sleep(7)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/main/div/div/div[4]/div/div/div[2]/div/form/div[1]/input").send_keys("let go")
driver.find_element(By.XPATH, "/html/body/main/div/div/div[4]/div/div/div[2]/div/form/div[3]/input").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/main/div/div/div[4]/div/div/div[2]/div/form/input").click()
time.sleep(9)
driver.close()
