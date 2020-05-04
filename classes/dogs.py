class Dog:
    species = "Canis familiaris"

    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age


def main():
    addie = Dog("border collie", "addie", 3)
    rex = Dog("terrier", "rex", 3)
    stuie = Dog("staffie", "stuie", "8")

    print(" {0} {1} {2}".format(addie.name, addie.breed,addie.age))
    print(" {0} {1} {2}".format(rex.name, rex.breed, rex.age))
    print(" {0} {1} {2}".format(stuie.name, stuie.breed, stuie.age))

    print(Dog.species)

if __name__ == "__main__":
    main()


