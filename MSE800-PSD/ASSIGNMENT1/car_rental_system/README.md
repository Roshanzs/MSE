# Car Rental System

This project is a Python and SQLite-based car rental management system. It supports user registration/login, car management, rental management, and more. It is suitable for learning and small business demonstrations.

---

## Directory Structure

```
car_rental_system/
├── car.py           # Car class definition
├── database.py      # Database operation interface (integrated with sqlite)
├── db.py            # SQLite database initialization and connection
├── main.py          # Main entry, console menu interaction
├── rental.py        # Rental class definition
├── user.py          # User, Admin, Customer class definitions
├── user_factory.py  # User factory class, creates users by role
├── README.md        # Documentation (Chinese)
├── README_en.md     # Documentation (English)
└── car_rental.db    # SQLite database file (auto-generated after running)
```

---

## Requirements
- Python 3.7 or above (Python 3.10+ recommended)
- No third-party libraries required, uses standard library sqlite3

---

## Installation & Setup

1. **Get the Code**
   - Place the car_rental_system folder in your working directory.

2. **Initialize the Database**
   - No manual steps needed. The car_rental.db database file will be created automatically on first run.

3. **Run the Program**
   - Open a terminal and go to the parent directory of car_rental_system (e.g., ASSIGNMENT1):
     ```bash
     cd ASSIGNMENT1
     python -m car_rental_system.main
     ```
   - If you get a module not found error, make sure there is an __init__.py file in car_rental_system (can be empty), or run directly:
     ```bash
     python car_rental_system/main.py
     ```

---

## Usage Guide

1. **Main Menu**
   - Register: Enter username, password, and role (admin/customer)
   - Login: Enter username and password to access the corresponding menu
   - Exit: Quit the program

2. **Admin Menu**
   - Add Car: Enter car info (ID, make, model, year, mileage, availability, rental period, price)
   - Update Car: Select car ID and field to modify
   - Delete Car: Enter car ID to delete
   - Approve Rentals: View all rentals, enter ID to approve/reject
   - View All Cars: Show all car information
   - Logout: Return to main menu

3. **Customer Menu**
   - View Available Cars: Show all available cars and prices
   - Book Car: Enter car ID, name, phone, rental dates
   - View My Rentals: Show all rental orders for the current user
   - Logout: Return to main menu

---

## File Descriptions

- **main.py**: Main entry, handles menu and flow control.
- **db.py**: Database initialization and connection management, auto table creation.
- **database.py**: All data CRUD interfaces, hides sqlite details.
- **user.py**: Defines user base class, admin and customer classes and their operations.
- **user_factory.py**: User factory, creates user objects by role.
- **car.py**: Car class, includes car attributes and display method.
- **rental.py**: Rental class, includes rental order attributes and fee calculation.
- **car_rental.db**: SQLite database file, stores all data.
- **README.md**: Documentation (Chinese).
- **README_en.md**: Documentation (English).

---

## FAQ

- **Database not generated?**
  - The car_rental.db file is created automatically on first run of main.py.
- **Module import error?**
  - Make sure to run `python -m car_rental_system.main` from the parent directory of car_rental_system.
- **How to reset data?**
  - Delete the car_rental.db file and rerun the program.

---

## Contact & Support
For questions or suggestions, please contact the developer or leave a comment in the code.
