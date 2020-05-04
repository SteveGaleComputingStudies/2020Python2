class Shark:
    animalType = "fish"    # class variable

 #constructor to set instance variables
    def __init__(self, type, teeth, fins):
        self.type = type
        self.teeth = teeth
        self.fins = fins



bullShark = Shark("bullshark", 200, 7)
whitePointer = Shark ("whitePointer", 300, 9)


print(" {0} {1} {2} ".format(bullShark.type,bullShark.teeth, bullShark.fins ))
print(Shark.animalType)
print(bullShark.animalType)

print(" {0} {1} {2} ".format(whitePointer.type,whitePointer.teeth, whitePointer.fins ))
