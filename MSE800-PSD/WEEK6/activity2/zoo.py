
from decorator import log_activity


class Zoo:
    def __init__(self, name, user=None):
        self.name = name
        self.animals = []
        self.user = user

    @log_activity
    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal} has been added to the zoo.")

    @log_activity
    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
            print(f"{animal} has been removed from the zoo.")
        else:
            print(f"{animal} is not in the zoo.")

    @log_activity
    def list_animals(self):
        print(f"Animals in {self.name} Zoo:")
        for animal in self.animals:
            print(f"{animal}")