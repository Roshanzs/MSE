
import zoo
from user import userLogin, userLogout


def main():

    user = None

    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        user = userLogin(username, password)
        if user:
            break

    Zoo1 = zoo.Zoo("City Zoo", user)

    while True:
        print("1 - add animal")
        print("2 - remove animal")
        print("3 - list animals")
        print("4 - logout")
        choice = input("Enter your choice: ")
        if choice == "1":
            animal = input("Enter animal name: ")
            Zoo1.add_animal(animal)
        elif choice == "2":
            animal = input("Enter animal name: ")
            Zoo1.remove_animal(animal)
        elif choice == "3":
            Zoo1.list_animals()
        elif choice == "4":
            userLogout(user)
            break
        else:
            print("Invalid choice. Please try again.")

    while True:
        logout = input("Do you want to logout? (yes/no): ")
        if logout.lower() == "yes":
            userLogout(user)
            break

    

if __name__ == "__main__":
    main()