class Shark:
    # Class variables
    animal_type = "fish"
    location = "ocean"
# Constructor method with instance variables name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age
 # Method with instance variable followers
    def set_followers(self, followers):
        self.followers = followers
        print("This user has " + str(followers) + " followers")

    def get_followers(self):
        return self.followers

def main():
    # First object, set up instance variables of constructor method
    sammy = Shark("Sammy", 5)
    # Print out instance variable name
    print(sammy.name)
    # Print out class variable location
    print(sammy.location)
    # Second object
    stephan = Shark("Stephan", 8)
    # Print out instance variable name
    print(stephan.name)
    # Use set_followers method and pass followers instance variable
    stephan.set_followers(77)
    # Print out class variable animal_type
    print(stephan.animal_type)

    #jessica

    jessica = Shark('Jessica',4)

    jessica.set_followers(87)
    print(" {0} {1} {2} ".format(jessica.name, jessica.age, jessica.followers))
    print(" {0} {1} {2} ".format(jessica.name, jessica.age, jessica.get_followers()))

    print(Shark.animal_type)
    print(Shark.location)




if __name__ == "__main__":
    main()


