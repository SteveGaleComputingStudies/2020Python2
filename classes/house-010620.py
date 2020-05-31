class House:

    type = "dwelling"
    location = "terrestrial"

    def __init__(self,name, buildingMaterial, size, storeys):
        self.name = name
        self.buildingMaterial = buildingMaterial
        self.size = size
        self.storeys = storeys

def main():
    H_29SmithSt = House("brick Veneer", " brick", 28, 2)
    H_31SmithSt = House("californian bungalow", " Timber", 18, 1)

    print (" {0} {1} {2} {3}".format(H_29SmithSt.name, H_29SmithSt.buildingMaterial, H_29SmithSt.size, H_29SmithSt.storeys))
    print (" {0} {1} {2} {3}".format(H_31SmithSt.name, H_31SmithSt.buildingMaterial, H_31SmithSt.size, H_31SmithSt.storeys))

if __name__ == "__main__":
    main()
