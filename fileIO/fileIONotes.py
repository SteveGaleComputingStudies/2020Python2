# make new textfile
# "w" is write, "r" is read, "a+" is append
file = open("testfile.txt","w")
#write to the file
file.write("1. New file?")
file.write("\n2. Second line ")
file.write("\n3. Still more")
file.write("\n4. The new line statements work in the text file.")
file.write("\n5. You can read it and print it out as well")
#read from the file and print
file =open("testfile.txt","r")
#read line 1
print(file.readline())
#print a set no of letters
print(file.read(16))
#read the rest of the contents of testfile.txt
print(file.read())
file.close()
#append
file = open("testfile.txt","a+")
file.write("\n6. Appended line ")
#change to read mode.
#Open file for reading
file =open("testfile.txt","r")
print(file.read())
file.close()
