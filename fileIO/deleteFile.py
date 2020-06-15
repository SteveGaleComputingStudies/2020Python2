import os

try:
    os.remove("fileIO\\files\\testfile2.txt")     # fileIO\\files\\testfile.txt relative to project base
except: 
    print("file not found")

