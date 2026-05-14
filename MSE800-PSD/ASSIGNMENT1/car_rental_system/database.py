
from .db import get_connection, init_db

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            init_db()
        return cls._instance

    # userassociated methods
    def add_user(self, username, password, role):
        conn = get_connection()
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
        conn.commit()
        conn.close()

    def get_user(self, username):
        conn = get_connection()
        c = conn.cursor()
        c.execute("SELECT username, password, role FROM users WHERE username=?", (username,))
        row = c.fetchone()
        conn.close()
        if row:
            return {'username': row[0], 'password': row[1], 'role': row[2]}
        return None

    # carassociated methods
    def add_car(self, car):
        conn = get_connection()
        c = conn.cursor()
        c.execute("INSERT INTO cars (car_id, make, model, year, mileage, available_now, min_period, max_period, price_per_day) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                  (car.car_id, car.make, car.model, car.year, car.mileage, int(car.available_now), car.min_period, car.max_period, car.price_per_day))
        conn.commit()
        conn.close()

    def update_car(self, car_id, **kwargs):
        conn = get_connection()
        c = conn.cursor()
        for k, v in kwargs.items():
            c.execute(f"UPDATE cars SET {k}=? WHERE car_id=?", (v, car_id))
        conn.commit()
        conn.close()

    def delete_car(self, car_id):
        conn = get_connection()
        c = conn.cursor()
        c.execute("DELETE FROM cars WHERE car_id=?", (car_id,))
        conn.commit()
        conn.close()

    def get_all_cars(self):
        conn = get_connection()
        c = conn.cursor()
        c.execute("SELECT car_id, make, model, year, mileage, available_now, min_period, max_period, price_per_day FROM cars")
        cars = c.fetchall()
        conn.close()
        return cars

    def get_car(self, car_id):
        conn = get_connection()
        c = conn.cursor()
        c.execute("SELECT car_id, make, model, year, mileage, available_now, min_period, max_period, price_per_day FROM cars WHERE car_id=?", (car_id,))
        car = c.fetchone()
        conn.close()
        return car

    # rentalassociated methods
    def add_rental(self, rental):
        conn = get_connection()
        c = conn.cursor()
        c.execute("INSERT INTO rentals (customer, car_id, start_date, end_date, name, phone, status, fee) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                  (rental.customer, rental.car_id, rental.start_date.strftime('%Y-%m-%d'), rental.end_date.strftime('%Y-%m-%d'), rental.name, rental.phone, rental.status, rental.fee))
        conn.commit()
        conn.close()

    def update_rental_status(self, rental_id, status):
        conn = get_connection()
        c = conn.cursor()
        c.execute("UPDATE rentals SET status=? WHERE rental_id=?", (status, rental_id))
        conn.commit()
        conn.close()

    def get_all_rentals(self):
        conn = get_connection()
        c = conn.cursor()
        c.execute("SELECT rental_id, customer, car_id, start_date, end_date, name, phone, status, fee FROM rentals")
        rentals = c.fetchall()
        conn.close()
        return rentals

    def get_rentals_by_customer(self, username):
        conn = get_connection()
        c = conn.cursor()
        c.execute("SELECT rental_id, customer, car_id, start_date, end_date, name, phone, status, fee FROM rentals WHERE customer=?", (username,))
        rentals = c.fetchall()
        conn.close()
        return rentals
