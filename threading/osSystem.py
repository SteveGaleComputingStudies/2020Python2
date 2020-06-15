# https://docs.python.org/3/library/os.html#os.system
import os

output = os.system("dir /w")        # use os.popen to get the directory contents returnes
print(output)   # 0 = sucessful

