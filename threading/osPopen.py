# https://docs.python.org/3/library/os.html#os.popen
import os

output = os.popen('dir /w').read()
print("dir /w :\n" + output)   # output = the contents of the listing