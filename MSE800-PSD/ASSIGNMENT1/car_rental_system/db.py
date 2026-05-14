import sqlite3

DB_PATH = "car_rental.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    c = conn.cursor()
    # 用户表
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )''')
    # 车辆表
    c.execute('''CREATE TABLE IF NOT EXISTS cars (
        car_id INTEGER PRIMARY KEY,
        make TEXT,
        model TEXT,
        year INTEGER,
        mileage INTEGER,
        available_now INTEGER,
        min_period INTEGER,
        max_period INTEGER,
        price_per_day REAL
    )''')
    # 租赁表
    c.execute('''CREATE TABLE IF NOT EXISTS rentals (
        rental_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer TEXT,
        car_id INTEGER,
        start_date TEXT,
        end_date TEXT,
        name TEXT,
        phone TEXT,
        status TEXT,
        fee REAL,
        FOREIGN KEY(car_id) REFERENCES cars(car_id),
        FOREIGN KEY(customer) REFERENCES users(username)
    )''')
    conn.commit()
    conn.close()
