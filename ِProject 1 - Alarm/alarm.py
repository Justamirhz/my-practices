import datetime
import time

class alarm():
    def userin(self,j):
        if j=="3":
         self.user_sec = input("tell me sec:")
        elif j=="2":
            self.user_m = int(input("tell me minite:"))   
    def calculate_seconds(self):
        now = datetime.datetime.now()
        final_s = now.second+int(self.user_sec)
        while True:
            current_s = datetime.datetime.now().second
            time.sleep(1)
            if final_s<=current_s:
                print("sound")
                break
    def calculate_m(self):
        now = datetime.datetime.now()
        final_m = now.minute+self.user_m
        print(now)
        print(final_m)
        time.sleep(1)
        while True:
            current_m = datetime.datetime.now().minute
            if final_m<=current_m:
                print("sound")
                break

alarm = alarm()
alarm.userin("3")
alarm.calculate_seconds()

