import sqlite3

def connect_db():
    return sqlite3.connect('exchange.db')

def create_customer_database():
    conn = connect_db()
    c = conn.cursor()
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL UNIQUE,
            age INTEGER NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

def create_transaction_database():
    conn = connect_db()
    c = conn.cursor()
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer INTEGER NOT NULL,
            bank_name TEXT NOT NULL,
            account TEXT NOT NULL,
            time DATETIME NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

def create_account_database():
    conn = connect_db()
    c = conn.cursor()
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            password TEXT NOT NULL,
            type TEXT NOT NULL,
            balance REAL NOT NULL,
            account_No TEXT NOT NULL UNIQUE
        )
    ''')
    
    conn.commit()
    conn.close()

def create_bank_database():
    conn = connect_db()
    c = conn.cursor()
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS banks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            country TEXT NOT NULL,
            bank_code TEXT NOT NULL UNIQUE,
            bank_location TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()


def create_money_database():
    conn = connect_db()
    c = conn.cursor()
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS money (
            currency_code TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            symbol TEXT NOT NULL,
            value REAL NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()