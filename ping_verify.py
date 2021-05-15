# typo error in import
import subprocess

for ping in range(1,255):
    address = "100.98.13." + str(ping)
    res = subprocess.call(['nslookup ', address])
    if res == 0:
        print("ping to", address, "OK")
    elif res == 2:
        print("no response from", address)
    else:
        print("ping to", address, "failed!")