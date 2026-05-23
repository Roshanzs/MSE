# Auckland Aquarium Management System

This project is a simple command-line system to manage an aquarium in Auckland, supporting the following fish categories:
- Goldfish
- Shark
- Angelfish
- Tuna
- Salmon

## Features
- Add fish to the aquarium by category and quantity
- Display the current number of each fish type
- Uses **Factory Pattern** to create fish objects
- Uses **Singleton Pattern** to ensure only one aquarium instance


## Example Usage

```
Welcome to Auckland Aquarium Management System!
Available fish: Goldfish, Shark, Angelfish, Tuna, Salmon

Enter 'add' to add fish, 'show' to display, 'exit' to quit: add
Enter fish type: Shark
Enter number of fish to add: 2
Added 2 Shark(s) to the aquarium.

Enter 'add' to add fish, 'show' to display, 'exit' to quit: show
Current fish in the aquarium:
Goldfish: 0
Shark: 2
Angelfish: 0
Tuna: 0
Salmon: 0
```
