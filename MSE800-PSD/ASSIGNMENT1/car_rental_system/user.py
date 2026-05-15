from abc import ABC, abstractmethod
from database import Database

class User(ABC):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @abstractmethod
    def get_role(self):
        pass

class Admin(User):
    def get_role(self):
        return "admin"

    def add_car(self, car):
        db = Database()
        db.add_car(car)
        print(f"Car {car.car_id} added.")

    def update_car(self, car_id, **kwargs):
        db = Database()
        db.update_car(car_id, **kwargs)
        print(f"Car {car_id} updated.")

    def delete_car(self, car_id):
        db = Database()
        db.delete_car(car_id)
        print(f"Car {car_id} deleted.")

    def manage_rental(self, rental_id, approve=True):
        db = Database()
        db.update_rental_status(rental_id, "approved" if approve else "rejected")
        print(f"Rental {rental_id} {'approved' if approve else 'rejected'}.")

class Customer(User):
    def get_role(self):
        return "customer"

    def view_cars(self):
        db = Database()
        for c in db.get_all_cars():
            if c[5]:
                print(f"{c[0]}: {c[1]} {c[2]} ({c[3]}), Mileage: {c[4]}, Price/Day: {c[8]}, Available: {bool(c[5])}")

    def book_car(self, car_id, start_date, end_date, name, phone):
        db = Database()
        car_row = db.get_car(car_id)
        if not car_row or not car_row[5]:
            print("Car not available.")
            return
        from .rental import Rental
        rental_id = None 
        rental = Rental(rental_id, self.username, car_id, start_date, end_date, name, phone)
        db.add_rental(rental)
        print(f"Rental request submitted.")
