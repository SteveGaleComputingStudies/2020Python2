class Shellfish:
    location = "ocean"
    skeleton = "exoskeleton"
    def __init__(self,shape ="spiral",type="snail"):
        self.shape = shape
        self.type = type


greenSnail = Shellfish("spiral","snail")
pippi = Shellfish("flat-plates","scallop")

print(greenSnail.shape + greenSnail.type)
print(pippi.location + pippi.type + pippi.shape)