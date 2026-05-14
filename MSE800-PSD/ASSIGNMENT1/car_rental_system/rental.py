from .database import Database


class Rental:
    def __init__(self, rental_id, customer, car_id, start_date, end_date, name, phone):
        self.rental_id = rental_id
        self.customer = customer
        self.car_id = car_id
        self.start_date = start_date
        self.end_date = end_date
        self.name = name
        self.phone = phone
        self.status = "pending"
        self.fee = self.calculate_fee()

    def calculate_fee(self):
        db = Database()
        car = db.cars.get(self.car_id)
        days = (self.end_date - self.start_date).days
        if car:
            return car.price_per_day * days
        else:
            return 0

    def __str__(self):
        return f"Rental {self.rental_id}: {self.car_id} by {self.customer} ({self.name}, {self.phone}) from {self.start_date} to {self.end_date}, Status: {self.status}, Fee: {self.fee}"
