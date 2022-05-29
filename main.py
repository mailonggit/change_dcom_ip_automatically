import os
import requests
from time import sleep 

os.system("rasdial /disconnect")
print("Disconnect mobile partner")
sleep(5)
#os.system("rasdial Name")
os.system("rasdial Lewis")
print("Connect mobile partner")
sleep(5)
ip = requests.get("https://api.ipify.org").text
print("ip: " + ip)