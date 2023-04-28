import datetime
import time


user_time = int(input("tell a sec:"))

now = datetime.datetime.now()

final_s = now.second+user_time


while True:
    current_s = datetime.datetime.now().second
    time.sleep(1) 
    if final_s<=current_s:
     print("sound!")
     exit()

