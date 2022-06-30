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
emil="rawr@knowledgemd.com"
options.add_argument('--no-first-run --no-service-autorun --password-store=basic') #wlacz to jak juz nie bedzie dev test
#options.user_data_dir = "rawr"
options.add_argument("--window-size=1920,1080")
#options.add_argument('--user-data-dir=rawr')
options.add_argument("--remote-debugging-port=38223")
driver = uc.Chrome(options=options, version_main=103)  # version_main allows to specify your chrome version instead of following chrome global version
driver.set_window_size(1000, 800)
driver.execute_script('window.open("https://mail.tm/","_blank");')
driver.switch_to.window(driver.window_handles[1])
print("rawr")
time.sleep(3)
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div[5]/button").click()
time.sleep(8)
print("yay")
emailgw = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div/input").get_attribute("value") #getemail
print(emailgw)
emailrepl = emailgw


usernamerepl = "".join(random.sample(username_for, long_username))
driver.switch_to.window(driver.window_handles[0])
driver.get("https://www.twitch.tv/")
time.sleep(10)
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div/div/div[3]/button/div/div/div').click()
time.sleep(20)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[2]/button").click()
time.sleep(12)
# rawr = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[2]/div/div[2]/input")
# driver.switch_to.frame(rawr)
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[2]/div/div[2]/input").send_keys("".join(random.sample(username_for, long_username)))
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/div[1]/div[2]/div[1]/input").send_keys("CloudKid123!Assxdr")
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/div[2]/div/div[2]/div[1]/input").send_keys("CloudKid123!Assxdr")
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[4]/div/div[2]/div[1]/select/option[5]").click()
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[4]/div/div[2]/div[2]/div/input").send_keys("18")
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[4]/div/div[2]/div[3]/div/input").send_keys("1999")
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[5]/div/div[2]/button/div/div[2]").click()
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[5]/div/div[1]/div[2]/input").send_keys(emailrepl)
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[6]/button").click()

time.sleep(10)



time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
time.sleep(6)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div[2]/ul/li/a").click()
time.sleep(3)
rawr = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div[3]/div[2]/div/iframe")
driver.switch_to.frame(rawr)
time.sleep(1)
xdr = driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr/td/center/table[2]/tbody/tr/td/table[4]/tbody/tr/th/table/tbody/tr/th[1]/center/table/tbody/tr/td/table/tbody/tr/td/a").get_attribute("href")
driver.switch_to.default_content()
driver.switch_to.window(driver.window_handles[0])
driver.get(xdr)
time.sleep(8)
driver.get("https://www.twitch.tv/bluezczatupl")
time.sleep(8)
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div/div/div[3]/button/div/div/div').click()
time.sleep(8)
driver.switch_to.default_content()
input("Rawr")
while True:
    lines = open('rawr.txt').read().splitlines()
    myline =random.choice(lines)
    print(myline)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div/div/section/div/div[4]/div[2]/div[1]/div[2]/div/div/div[1]/div/div/div/div/div[2]").send_keys(myline+Keys.ENTER)
    time.sleep(15)
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.close()
