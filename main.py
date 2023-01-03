import os, time

host = "8.8.8.8"
period = 30
f = open("results.txt", "w")

def check_ping(host_ip):
    response = os.system("ping -n 1 " + host_ip)
    if response == 0:
        return "Network Active"
    else:
        return "Network Error"

while True:
    time.sleep(period)
    now = time.localtime()
    if check_ping(host) == "Network Active":
        f.write(time.strftime("%d/%m/%Y %H:%M:%S", now) + "\t" + "Network Error" + "\n")
    else:
        continue