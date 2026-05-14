

from datetime import datetime, timedelta
from car_rental_system.user_factory import UserFactory
from car_rental_system.car import Car
from car_rental_system.database import Database

def register(username, password, role):
    db = Database()
    if db.get_user(username):
        print("Username already exists.")
        return None
    db.add_user(username, password, role)
    user = UserFactory.create_user(role, username, password)
    print(f"{role.capitalize()} {username} registered.")
    return user

def login(username, password):
    db = Database()
    user_row = db.get_user(username)
    if user_row and user_row['password'] == password:
        user = UserFactory.create_user(user_row['role'], user_row['username'], user_row['password'])
        print(f"{user.get_role().capitalize()} {username} logged in.")
        return user
    else:
        print("Invalid credentials.")
        return None

def main_menu():
    print("\n==== Car Rental System ====")
    print("1. register")
    print("2. login")
    print("3. logout")
    return input("please choose an option: ")

def user_menu(user):
    if user.get_role() == "admin":
        return admin_menu(user)
    else:
        return customer_menu(user)

def admin_menu(admin):
    while True:
        print("\n==== Admin Menu ====")
        print("1. Add Car")
        print("2. Update Car")
        print("3. Delete Car")
        print("4. Approve Rental")
        print("5. View All Cars")
        print("6. Logout")
        choice = input("please choose an option: ")
        if choice == "1":
            while True:
                try:
                    car_id = int(input("Car ID: "))
                    break
                except ValueError:
                    print("Car ID must be an integer!")
            make = input("Brand: ")
            model = input("Model: ")
            while True:
                try:
                    year = int(input("Year: "))
                    break
                except ValueError:
                    print("Year must be an integer!")
            while True:
                try:
                    mileage = int(input("Mileage: "))
                    break
                except ValueError:
                    print("Mileage must be an integer!")
            while True:
                yn = input("Available now (y/n): ").lower()
                if yn in ['y', 'n']:
                    available_now = yn == 'y'
                    break
                else:
                    print("Please enter y or n!")
            while True:
                try:
                    min_period = int(input("Minimum rental period (days): "))
                    break
                except ValueError:
                    print("Minimum rental period must be an integer!")
            while True:
                try:
                    max_period = int(input("Maximum rental period (days): "))
                    break
                except ValueError:
                    print("Maximum rental period must be an integer!")
            while True:
                try:
                    price_per_day = float(input("Price per day: "))
                    break
                except ValueError:
                    print("Price per day must be a number!")
            car = Car(car_id, make, model, year, mileage, available_now, min_period, max_period, price_per_day)
            db = Database()
            db.add_car(car)
            print(f"Car {car_id} added.")
        elif choice == "2":
            while True:
                try:
                    car_id = int(input("Car ID: "))
                    break
                except ValueError:
                    print("Car ID must be an integer!")
            field = input("Field to update (make/model/year/mileage/available_now/min_period/max_period/price_per_day): ")
            value = input("New value: ")
            if field in ["year", "mileage", "min_period", "max_period"]:
                try:
                    value = int(value)
                except ValueError:
                    print("This field must be an integer!")
                    return
            if field == "available_now":
                if value.lower() not in ['y', 'n']:
                    print("Please enter y or n!")
                    return
                value = value.lower() == 'y'
            if field == "price_per_day":
                try:
                    value = float(value)
                except ValueError:
                    print("Price per day must be a number!")
                    return
            db = Database()
            db.update_car(car_id, **{field: value})
            print(f"Car {car_id} updated.")
        elif choice == "3":
            while True:
                try:
                    car_id = int(input("Car ID: "))
                    break
                except ValueError:
                    print("Car ID must be an integer!")
            db = Database()
            db.delete_car(car_id)
            print(f"Car {car_id} deleted.")
        elif choice == "4":
            db = Database()
            for r in db.get_all_rentals():
                print(f"Rental {r[0]}: {r[2]} by {r[1]} ({r[5]}, {r[6]}) from {r[3]} to {r[4]}, Status: {r[7]}, Fee: {r[8]}")
            while True:
                try:
                    rental_id = int(input("Rental ID to approve/reject: "))
                    break
                except ValueError:
                    print("Rental ID must be an integer!")
            while True:
                yn = input("Approve (y) or reject (n): ").lower()
                if yn in ['y', 'n']:
                    approve = yn == 'y'
                    break
                else:
                    print("Please enter y or n!")
            db.update_rental_status(rental_id, "approved" if approve else "rejected")
            print(f"Rental {rental_id} {'approved' if approve else 'rejected'}.")
        elif choice == "5":
            db = Database()
            print("\n--- All Cars ---")
            for c in db.get_all_cars():
                print(f"{c[0]}: {c[1]} {c[2]} ({c[3]}), Mileage: {c[4]}, Price/Day: {c[8]}, Available: {bool(c[5])}")
        elif choice == "6":
            print("Logged out.\n")
            break
        else:
            print("Invalid choice")

def customer_menu(customer):
    while True:
        print("\n==== Customer Menu ====")
        print("1. View Available Cars")
        print("2. Rent a Car")
        print("3. View My Rentals")
        print("4. Log Out")
        choice = input("Please select an option: ")
        if choice == "1":
            db = Database()
            for c in db.get_all_cars():
                if c[5]:
                    print(f"{c[0]}: {c[1]} {c[2]} ({c[3]}), Mileage: {c[4]}, Price/Day: {c[8]}, Available: {bool(c[5])}")
        elif choice == "2":
            while True:
                try:
                    car_id = int(input("Car ID: "))
                    break
                except ValueError:
                    print("Car ID must be an integer!")
            while True:
                name = input("Your Name: ")
                if len(name.strip()) == 0:
                    print("Name cannot be empty!")
                else:
                    break
            while True:
                phone = input("Phone Number: ")
                if not phone.isdigit() or len(phone) < 7:
                    print("Phone number must be a 7-digit or longer numeric string!")
                else:
                    break
            while True:
                start = input("Start Date (YYYY-MM-DD): ")
                try:
                    start_date = datetime.strptime(start, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Invalid date format, please use YYYY-MM-DD!")
            while True:
                end = input("End Date (YYYY-MM-DD): ")
                try:
                    end_date = datetime.strptime(end, "%Y-%m-%d")
                    if end_date <= start_date:
                        print("End date must be later than start date!")
                        continue
                    break
                except ValueError:
                    print("Invalid date format, please use YYYY-MM-DD!")
            db = Database()
            car_row = db.get_car(car_id)
            if not car_row or not car_row[5]:
                print("Car not available.")
                return
            from car_rental_system.rental import Rental
            rental_id = None 
            rental = Rental(rental_id, customer.username, car_id, start_date, end_date, name, phone)
            db.add_rental(rental)
            print(f"Rental request submitted.")
        elif choice == "3":
            db = Database()
            for r in db.get_rentals_by_customer(customer.username):
                print(f"Rental {r[0]}: {r[2]} by {r[1]} ({r[5]}, {r[6]}) from {r[3]} to {r[4]}, Status: {r[7]}, Fee: {r[8]}")
        elif choice == "4":
            print("Logged out.\n")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    db = Database()
    # preset admin account
    if not db.get_user("admin1"):
        register("admin1", "adminpass", "admin")
    current_user = None
    while True:
        choice = main_menu()
        if choice == "1":
            while True:
                username = input("Username: ")
                if len(username.strip()) == 0:
                    print("Username cannot be empty!")
                else:
                    break
            while True:
                password = input("Password: ")
                if len(password) < 4:
                    print("Password must be at least 4 characters long!")
                else:
                    break
            while True:
                role = input("Role (admin/customer): ").lower()
                if role not in ["admin", "customer"]:
                    print("Role must be either 'admin' or 'customer'!")
                else:
                    break
            register(username, password, role)
        elif choice == "2":
            username = input("Username: ")
            password = input("Password: ")
            user = login(username, password)
            if user:
                user_menu(user)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")
