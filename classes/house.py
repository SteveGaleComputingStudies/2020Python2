class House:

    type = "dwelling"
    location = "terrestrial"

    def __init__(self,name, buildingMaterial, size, storeys):
        self.name = name
        self.buildingMaterial = buildingMaterial
        self.size = size
        self.storeys = storeys

def main():
    bv = House("brick Veneer", " brick", 28, 2)
    calBungalow = House("californian bungalow", " Timber", 18, 1)

    print (" {0} {1} {2} {3}".format(bv.name, bv.buildingMaterial, bv.size, bv.storeys))
    print (" {0} {1} {2} {3}".format(calBungalow.name, calBungalow.buildingMaterial, calBungalow.size, calBungalow.storeys))

if __name__ == "__main__":
    main()
