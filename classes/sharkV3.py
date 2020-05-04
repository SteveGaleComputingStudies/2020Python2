class Shark:
    animalType = "fish"    # class variable

 #constructor to set instance variables
    def __init__(self, type, teeth, fins):
        self.type = type
        self.teeth = teeth
        self.fins = fins

# good programming practice to use instance get and set methods
    def setColour(self, colour):
        self.colour = colour

    def getColour(self):
        return self.colour



def main():
    bullShark = Shark("bullshark", 200, 7)

    whitePointer = Shark ("whitePointer", 300, 9)


    print(" {0} {1} {2} ".format(bullShark.type,bullShark.teeth, bullShark.fins ))
    print(Shark.animalType)
    print(bullShark.animalType)

    print(" {0} {1} {2} ".format(whitePointer.type,whitePointer.teeth, whitePointer.fins ))

# use get and set methode
    bullShark.setColour("brown")
    whitePointer.setColour("white/gray")

    print (" shark colours {0} {1} : {2} {3}".format(bullShark.type,bullShark.getColour(),whitePointer.type,whitePointer.getColour() ))

if __name__ == "__main__":
 main()
