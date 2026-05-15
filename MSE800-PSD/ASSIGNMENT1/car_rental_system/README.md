# Car Rental System

This project is a Python and SQLite-based car rental management system. It supports user registration/login, car management, rental management, and more. It is suitable for learning and small business demonstrations.

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
└── car_rental.db    # SQLite database file (auto-generated after running)
```

## Requirements
- Python 3.12 or above (Python 3.12+ recommended)
- No third-party libraries required, uses standard library sqlite3

## Installation & Setup

1. **Get the Code**
   - Place the car_rental_system folder in your working directory.

2. **Initialize the Database**
   - No manual steps needed. The car_rental.db database file will be created automatically on first run.

3. **Run the Program**
   - Open a terminal and go to the parent directory of car_rental_system (e.g., ASSIGNMENT1):
     ```bash
     cd ASSIGNMENT1
     cd car_rental_system
     python main.py
     ```

## Usage Guide

1. **Main Menu**
   - Register: Enter username, password, and role (admin/customer)
   - Login: Enter username and password to access the corresponding menu
   - logout: Quit the program

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

## File Descriptions

- **main.py**: Main entry, handles menu and flow control.
- **db.py**: Database initialization and connection management, auto table creation.
- **database.py**: All data CRUD interfaces, hides sqlite details.
- **user.py**: Defines user base class, admin and customer classes and their operations.
- **user_factory.py**: User factory, creates user objects by role.
- **car.py**: Car class, includes car attributes and display method.
- **rental.py**: Rental class, includes rental order attributes and fee calculation.
- **car_rental.db**: SQLite database file, stores all data.
- **README.md**: Documentation.


## Innovation & Improvement Plan

**Mobile App Integration:**
To enhance user convenience and competitiveness, the system can be extended with a mobile app (iOS/Android). This app would allow users to:
- Browse and book cars anytime, anywhere
- Receive real-time notifications for booking status
- Manage their rentals and profiles on the go
- Use QR code or NFC for contactless car pickup/return

**Cloud Services & Smart Devices:**
- Integrate with cloud for data backup and analytics
- Connect with IoT devices (e.g., smart locks, GPS) for automated car access and tracking

These innovations will greatly improve user experience and provide a competitive edge in the car rental market.

## Future Development Roadmap

1. **RESTful API**: Develop a web API for integration with mobile/web clients.
2. **Mobile App**: Launch official apps for iOS and Android.
3. **Online Payment**: Integrate payment gateways for seamless transactions.
4. **Data Analytics**: Add dashboards for business insights and fleet optimization.
5. **AI Recommendations**: Use machine learning to recommend cars and optimize pricing.
6. **Multi-language Support**: Expand to support more languages and regions.

## Update, Bug Fix, and Feature Addition Policy

- All updates and new features are developed in feature branches and merged after code review and testing.
- Bug fixes are prioritized and released as soon as possible, with clear release notes.
- Major changes are backward compatible whenever possible; breaking changes are documented and versioned.
- Database migrations are handled with scripts and backups to ensure data safety.

## Software Maintenance, Version Control, and Backward Compatibility

- **Version Control**: Git is used for all code management. The main branch is always stable; development and features use separate branches.
- **Semantic Versioning**: Releases follow MAJOR.MINOR.PATCH format (e.g., v1.2.0).
- **Backward Compatibility**: Public interfaces and database schemas are maintained for compatibility. Deprecated features are marked and removed only in major releases.
- **Documentation**: All changes, especially breaking ones, are documented in the README and release notes.

## Contact & Support
For questions or suggestions, please contact the developer or leave a comment in the code.
