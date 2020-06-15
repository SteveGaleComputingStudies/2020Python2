try:
    f = open("fileIO\\files\\testfile2.txt")     # fileIO\\files\\testfile.txt relative to project base
    print(f.read())
except: 
    print("file not found")
