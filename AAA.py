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
os.system("rm -rf rawr && cp -r rawrz rawr")
options = uc.ChromeOptions()
a = True
low_word = "abcdefghijklkmnopqrstuvwxyz"
upper_word = "ABDCEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
symbols = "!@#$%&*"
username_for = low_word
password_for = low_word + upper_word + number + symbols
long_password = 16
long_username = 12
options.add_argument('--no-first-run --no-service-autorun --password-store=basic') #wlacz to jak juz nie bedzie dev test
options.user_data_dir = "rawr"
options.add_argument("--window-size=1920,1080")
options.add_argument('--user-data-dir=rawr')
options.add_argument("--remote-debugging-port=38223")
driver = uc.Chrome(options=options, version_main=103)  # version_main allows to specify your chrome version instead of following chrome global version
driver.set_window_size(1920, 1080)
driver.execute_script('''window.open("https://konto-pocztowe.interia.pl/#/nowe-konto/darmowe","_blank");''')
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/button[3]").click()
time.sleep(1)
usernamerepl = "".join(random.sample(username_for, 6))
usernamerepl1 = "".join(random.sample(username_for, 6))
ass = "".join(random.sample(username_for, 12))
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[1]/input').send_keys(usernamerepl)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[2]/input').send_keys(usernamerepl1)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[3]/div[1]/input').send_keys("21")
time.sleep(0.5)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[3]/div[2]/label").click()
time.sleep(0.5)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[3]/div[2]/ul/li[3]").click()
time.sleep(0.5)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[3]/div[3]/input").send_keys("1999")
time.sleep(0.5)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[4]/label").click()
time.sleep(0.5)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[4]/ul/li[1]").click()
time.sleep(0.5)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[5]/div[1]/input").click()
time.sleep(0.5)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[6]/div/input").send_keys(ass+"!H")
time.sleep(0.5)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[7]/div/input").send_keys(ass+"!H")
time.sleep(0.5)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/form/div[2]/div[1]/div[1]/label/div").click()
time.sleep(0.5)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/form/div[2]/button").click()
rawr = usernamerepl+"."+usernamerepl1+"@interia.pl"

driver.switch_to.window(driver.window_handles[0])
driver.get("https://www.atlassian.com/software/bitbucket/bundle")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/main/div[3]/div/div[2]/div[5]/div/div/div[1]/span").click()
time.sleep(4)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[2]/div/section/div[2]/form/div[1]/div/div/div/input").send_keys(rawr)
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="signup-submit"]').click()
time.sleep(60)
driver.switch_to.window(driver.window_handles[1])
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[2]/section[3]/div[1]/div[1]/section/ul/li[1]/div[2]/div[1]").click()
time.sleep(4)
iframu = driver.find_element(By.XPATH, "/html/body/div[2]/section[1]/div/div/div/div[1]/div/div[3]/iframe")
driver.switch_to.frame(iframu)
egg = driver.find_element(By.XPATH, "/html/body/table/tbody/tr/td/div/div/div[2]/a").get_attribute("href")
driver.switch_to.default_content()
time.sleep(1)
driver.switch_to.window(driver.window_handles[0])
driver.get(egg)
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[2]/div/section/div[2]/form/div[2]/div/div/div/input").send_keys("CloudKid")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[2]/div/section/div[2]/form/div[3]/div[1]/div/div/div/div/input").send_keys(ass+"!H")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[2]/div/section/div[2]/form/div[6]/button").click()
time.sleep(45)
driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div[1]/div[2]/form[1]/div[2]/input").send_keys(usernamerepl+usernamerepl1)
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div[1]/div[2]/form[1]/p/button").click()
time.sleep(45)
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div[2]/div[5]/a/span/span/span").click()
time.sleep(2)
driver.get("https://bitbucket.org/repo/import")
time.sleep(4)
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/section/div/form/div[1]/input").send_keys("https://bitbucket.org/dfhsregfgxcv/rawr/src/master/")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/section/div/form/div[4]/div[1]/div[2]/span/input[1]").send_keys("".join(random.sample(username_for, 6)))
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/section/div/form/div[4]/div[2]/input").send_keys("".join(random.sample(username_for, 6)))
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/section/div/form/div[5]/div/button").click()
time.sleep(21)




driver.get("https://circleci.com/signup/")
time.sleep(4)
try:
  driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/a[2]").click()
except:
  pass
time.sleep(2)
try:
  driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/section/div[2]/div/div/div[2]/div[3]/button").click()
except:
  pass
try:
  driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/section/div[2]/div/div/div[2]/div[3]/button").click()
except:
  pass
time.sleep(45)
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/section/form/div/div/button[1]").click()
time.sleep(53)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/section[1]/div/div[2]/button").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/section[1]/div/div[2]/div/div/ul/li").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/section[2]/div/div[2]/button").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/section[2]/div/div[2]/div/div/ul/li").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/section[3]/div/div[2]/button[1]/div[2]/div[2]/input").send_keys("master")
time.sleep(7)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/button").click()
time.sleep(69)
