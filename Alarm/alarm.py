
import datetime
import time

# which = input("hour or minite or sec?")
# print("1-hour \n 2-minite \n 3-sec")



user_time = int(input("tell a sec:"))

now = datetime.datetime.now()

final_s = now.second+user_time


while True:
    current_m = datetime.datetime.now().minute
    current_h = datetime.datetime.now().hour
    current_s = datetime.datetime.now().second


    # print(current_h)
    # print(current_m)
    # print(current_s)
    time.sleep(1) 
    if final_s<=current_s:
     print("sound!")
     exit()


