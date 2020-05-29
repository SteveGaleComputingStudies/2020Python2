num1 = 10
num2 = int(input(" divide number"))

try:
    num3 = num1 / num2
    print(num3)
except ZeroDivisionError:
    print("ZeroDivisionError")
except:
    print("error")

