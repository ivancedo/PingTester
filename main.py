import os, time

file = open("results.txt", "w")
host = "8.8.8.8"
period = 2
active_msg = "Network Active"
error_msg = "Network Error"

def check_ping(host_ip):
    response = os.system("ping -n 1 " + host_ip)
    if response == 0:
        return active_msg
    else:
        return error_msg

while True:
    time.sleep(period)
    now = time.localtime()
    if check_ping(host) == error_msg:
        file.write(time.strftime("%d/%m/%Y %H:%M:%S", now) + "\t" + error_msg + "\n")
    else:
        continue