# https://www.ictshore.com/python/python-ping-tutorial/
import os

hosts = ["10.0.0.138","10.0.0.150"] # list of host addresses

for host in hosts:
    os.system('ping ' + host)


