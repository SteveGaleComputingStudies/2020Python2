class Tree:
    def __init__(self,name,fruit):
        self.name = name
        self.fruit = fruit

    def essentialOil(self):
        print(self.name+" " +self.fruit+" This plant can be used in the production of essential oils")

class Eucalyptus(Tree):
    def essentialOil(self):
        print(self.name+" " +self.fruit+" is Volatile")

class Pear(Tree):
    def beverage(self):
        print(self.name+" " +self.fruit+" makes Pear cyder")

galaApple = Tree("Gala","Apple")
galaApple.essentialOil()

ash = Eucalyptus("ash","gumnut")
ash.essentialOil()

pecham = Pear("pecham","pear")
pecham.essentialOil()
pecham.beverage()