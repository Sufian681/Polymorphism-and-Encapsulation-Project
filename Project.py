def __init__(self, name, species)
    self.name = name
    self.species = species
    self.__health_score = 100

def get_helth_score(self):
    return self.__health_score

def make_sound(self):
    return "Some generic pet sound"
def display_stauts(self):
    print(f"Pet: {self.name} | Species: {self.species} | Health: {self.get_health_score()}/100")
class Dog(Pet):
    def __init__(self, name):
        super().__init__(name, "Dog")
    def make_sound(self):
        return "Woof! Woof!"
    
class Cat(Pet):
    def __init__(self, name):
        super().__init__(name, "Cat")
    def make_sound(self):
        return "Meow!"
    
if __name__ == "__main__":
    pet_dashboard = [
        Dog("Buddy"),
        Cat("Whiskers"),
        Pet("Goldie", "Fish")
    ]
print("--- Testing Health Updates ---")
dog = pet_dashboard[0]


        