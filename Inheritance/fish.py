class Fish:
    def __init__(self, first_name, last_name="Fish"):
        self.first_name = first_name
        self.last_name = last_name
    def swim(self):
        print("The fish is swimming.")
    def swim_backwards(self):
        print("The fish can swim backwards.")

class Trout(Fish):
    pass

class Clownfish(Fish):
    def live_with_anemone(self):
        print("The clownfish is coexisting with sea anemone.")

class Shark(Fish):
    def __init__(self, first_name, last_name="Shark",
        skeleton="cartilage", eyelids=True):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids
    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")



terry = Trout("Terry","Trout")
print(terry.first_name + " " + terry.last_name)
terry.swim()
terry.swim_backwards()


carrie = Clownfish("Casey")     # carrie?
print(carrie.first_name + " " + carrie.last_name)
carrie.swim()
carrie.live_with_anemone()


sammy = Shark("Sammy")
print(sammy.first_name + " " + sammy.last_name)
sammy.swim()
sammy.swim_backwards()
print(sammy.eyelids)
print(sammy.skeleton)
