# Define the base class 'Dog'
class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def get_info(self):
        print(f"{self.name}'s coat color is {self.coat_color}.")


# Create a child class 'JackRussellTerrier' inherited from 'Dog'
class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, energy_level):
        super().__init__(name, age, coat_color)
        self.energy_level = energy_level

    def special_skill(self):
        print(f"{self.name} has a special skill: High energy level!")

    def description(self):
        super().description()
        print(f"{self.name} is a Jack Russell Terrier.")


# Create a child class 'Bulldog' inherited from 'Dog'
class Bulldog(Dog):
    def __init__(self, name, age, coat_color, weight):
        super().__init__(name, age, coat_color)
        self.weight = weight

    def special_skill(self):
        print(f"{self.name} has a special skill: Strong and sturdy build!")

    def description(self):
        super().description()
        print(f"{self.name} is a Bulldog.")


# Create objects and implement the functionalities
dog1 = JackRussellTerrier("Buddy", 3, "White and Brown", "High")
dog2 = Bulldog("Rocky", 5, "Red", "Heavy")

# Describe the dogs
dog1.description()
dog2.description()

# Get information about the dogs' coat color
dog1.get_info()
dog2.get_info()

# Call the special skills of the dogs
dog1.special_skill()
dog2.special_skill()
