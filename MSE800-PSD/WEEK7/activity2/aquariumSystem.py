

# Auckland Aquarium Management System
from abc import ABC, abstractmethod
from aquarium_storage import AquariumStorage

class Fish(ABC):
	@abstractmethod
	def category(self):
		pass

class Goldfish(Fish):
	def category(self):
		return "Goldfish"

class Shark(Fish):
	def category(self):
		return "Shark"

class Angelfish(Fish):
	def category(self):
		return "Angelfish"

class Tuna(Fish):
	def category(self):
		return "Tuna"

class Salmon(Fish):
	def category(self):
		return "Salmon"

# factory pattern to create fish instances
class FishFactory:
	@staticmethod
	def create_fish(fish_type):
		fish_type = fish_type.lower()
		if fish_type == "goldfish":
			return Goldfish()
		elif fish_type == "shark":
			return Shark()
		elif fish_type == "angelfish":
			return Angelfish()
		elif fish_type == "tuna":
			return Tuna()
		elif fish_type == "salmon":
			return Salmon()
		else:
			raise ValueError(f"Unknown fish type: {fish_type}")

# instantiate aquarium as a singleton to manage fish counts
class Aquarium:
	_instance = None

	def __new__(cls):
		if cls._instance is None:
			cls._instance = super(Aquarium, cls).__new__(cls)
			cls._instance.storage = AquariumStorage()
		return cls._instance

	def add_fish(self, fish_type, count=1):
		self.storage.add_fish(fish_type, count)

	def display(self):
		print("\nCurrent fish in the aquarium:")
		for fish, count in self.storage.get_all():
			print(f"{fish}: {count}")

	def close(self):
	    self.storage.close()

def main():
    aquarium = Aquarium()
    print("Welcome to Auckland Aquarium Management System!")
    print("Available fish: Goldfish, Shark, Angelfish, Tuna, Salmon")
    try:
        while True:
            action = input("\nEnter 'add' to add fish, 'show' to display, 'exit' to quit: ").strip().lower()
            if action == 'add':
                fish_type = input("Enter fish type: ").strip().capitalize()
                try:
                    fish = FishFactory.create_fish(fish_type)
                except ValueError as e:
                    print(e)
                    continue
                try:
                    count = int(input("Enter number of fish to add: "))
                    if count < 1:
                        print("Count must be positive.")
                        continue
                except ValueError:
                    print("Invalid number.")
                    continue
                aquarium.add_fish(fish.category(), count)
                print(f"Added {count} {fish.category()} to the aquarium.")
            elif action == 'show':
                aquarium.display()
            elif action == 'exit':
                print("Exiting system. Goodbye!")
                break
            else:
                print("Unknown command.")
    finally:
        aquarium.close()

if __name__ == "__main__":
	main()




