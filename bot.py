import undetected_chromedriver as uc
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import json
import os
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
options.add_argument("--window-size=1920,1080")
options.add_argument('--user-data-dir=rawr')
options.add_argument("--remote-debugging-port=38223")
driver = uc.Chrome(options=options)  # version_main allows to specify your chrome version instead of following chrome global version
driver.set_window_size(1920, 1080)

print("rawr")
usernamerepl = "".join(random.sample(username_for, long_username))
emailrepl = "".join(random.sample(username_for, long_username))+"@cldkid.com"
a = True
time.sleep(3)
driver.get('https://replit.com/logout')
driver.switch_to.window(driver.window_handles[0])
time.sleep(1)
driver.get('https://replit.com/signup?from=landing')
time.sleep(3)
driver.find_element_by_xpath("/html/body/div/div/div[2]/main/div/form/div/div[2]/div/input").send_keys(usernamerepl)
time.sleep(1)
driver.find_element_by_xpath("/html/body/div/div/div[2]/main/div/form/div/div[3]/div/input").send_keys(emailrepl)
time.sleep(1)
driver.find_element_by_xpath("/html/body/div/div/div[2]/main/div/form/div/div[4]/div/input").send_keys(passwordrepl)
time.sleep(1)
driver.find_element_by_xpath("/html/body/div/div/div[2]/main/div/form/div/div[5]/button").click()
time.sleep(1)
timez = int(time.time())+300
while a==True:
    try:
        if(driver.find_element_by_xpath("/html/body/div/div/div[2]/main/div/form/div/div[5]/button/span").text=="Create account"):
            time.sleep(1)
            driver.find_element_by_xpath("/html/body/div/div/div[2]/main/div/form/div/div[5]/button").click()
    except:
        pass
    if(timez<int(time.time())):
        cockz
    if(driver.current_url.startswith("https://replit.com/signup")):
        time.sleep(0.4)
    else:
        a = False




driver.get('https://replit.com/@dsfjoh/LividUntrueInterface?v=1')
driver.execute_script("""function getElementByXpath(path){return document.evaluate(path,document,null,XPathResult.FIRST_ORDERED_NODE_TYPE,null).singleNodeValue}getElementByXpath("/html/body/div[1]/div/main/div[3]/div/div/div[2]/div/button[1]").click();""")
time.sleep(55)

driver.execute_script("""function getElementByXpath(path){return document.evaluate(path,document,null,XPathResult.FIRST_ORDERED_NODE_TYPE,null).singleNodeValue}getElementByXpath("/html/body/div[1]/div/div/main/div[2]/div/div/div[1]/header/div/div[2]/div/div/div").click();""")
#driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/button").click()
# time.sleep(2)
#driver.execute_script("""function getElementByXpath(path){return document.evaluate(path,document,null,XPathResult.FIRST_ORDERED_NODE_TYPE,null).singleNodeValue}getElementByXpath("/html/body/div[1]/div/div/main/div[2]/div/div/div[1]/header/div/div[2]/div/div").click();""")
# driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div[2]/div/div/div[1]/header/div/div[2]/div/div/div")
print("rawr")
#driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div[2]/div/div/div[1]/header/div/div[2]/div/div").click() #click run

time.sleep(30)
time.sleep(50)
# time.sleep(15)
# if driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div[2]/div/div/div[1]/header/div/div[2]/div/div/div").text == "START":
#     driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div[2]/div/div/div[1]/header/div/div[2]/div/div/div").click()
# time.sleep(2)
# if driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div[2]/div/div/div[1]/header/div/div[2]/div/div/div").text == "START":
#     driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div[2]/div/div/div[1]/header/div/div[2]/div/div/div").click()
# try:
#     driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div[2]/div/div/div[1]/header/div/div[2]/div/div/div").click() #click run
# except:
#     pass
# time.sleep(10)
# try: /html/body/div[3]/div/div[1]/button
#     driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div[2]/div/div/div[1]/header/div/div[2]/div/div/div").click() #click run
# except:
# #     pass
# time.sleep(50)
# print("waiting: 150")
# time.sleep(50)
# print("waiting: 100")
# if driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div[2]/div/div/div[1]/header/div/div[2]/div/div/div").text == "START":
#     driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div[2]/div/div/div[1]/header/div/div[2]/div/div/div").click()

import requests

namerepl = driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div[2]/div/div/div[1]/header/div/div[1]/span/div/div/div[1]/span[3]/span").text
username = driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div[2]/div/div/div[1]/header/div/div[1]/span/div/div/div[1]/span[1]/span/a").text
namerepl = namerepl.replace(".", "")
print(namerepl)
print(username)







url_i_name = "http://"+namerepl+"."+username+".repl.co"

# apikey = apikey_val["apikey"]
# botz = apikey_val["amount"]+1



# payload = "api_key="+apikey+"&format=json&type=1&url="+url_i_name+"&friendly_name="+url_i_name
# update_file(apikey, botz)
# headers = {
#     'cache-control': "no-cache",
#     'content-type': "application/x-www-form-urlencoded"
#     }
# response = requests.request("POST", url, data=payload, headers=headers)
# print(response.text)


payload = "test="+url_i_name
headers = {
    'cache-control': "no-cache",
    'content-type': "application/x-www-form-urlencoded"
    }
response = requests.request("POST", "https://rawrz.nordalts.cf/rawr", data=payload, headers=headers)
print(response)


time.sleep(3)


#driver.find_element(by=By.XPATH,value="/html/body/reach-portal/div[3]/div/div/div/div[2]/button").click()
#driver.find_element(by=By.XPATH,value="/html/body/reach-portal/div[3]/div/div/div/div[2]/button").send_keys(namerepl)
