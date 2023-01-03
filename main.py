import os, time

google_ip = "8.8.8.8"
period = 30
f = open("results.txt", "w")

def check_ping(host_ip):
    response = os.system("ping -n 1 " + host_ip)
    if response == 0:
        result = "Network Active"
    else:
        result = "Network Error"
    return result

while True:
    time.sleep(period)
    now = time.localtime()
    f.write(time.strftime("%d/%m/%Y %H:%M:%S", now) + "\t" + check_ping(google_ip) + "\n")
