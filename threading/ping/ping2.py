import os

hostnames = [
    '10.0.0.150',
    '10.0.0.138',
    '10.0.0.68',
]

for hostname in hostnames:
    response = os.system('ping -c 1 ' + hostname)   # note always returns 0 response in windows
    if response == 0:
        print( hostname + ' is up')
    else:
        print( hostname + ' is down')                # does not work in windows