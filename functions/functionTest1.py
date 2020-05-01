

def getUserInfo(displayStr = "enter a value"):
    number = int(input(displayStr))
    return(number)

def displayUserInfo():
    pass

def calculation(x,y):
    result = x + y
    return(result)

def endProgram():
    pass

number1 = getUserInfo("enter first value")
number2 = getUserInfo("enter second value")
displayUserInfo()
print(calculation(number1,number2))
getUserInfo()
endProgram()