
from services import UserService

def main():
    """Main function to run the user authentication system with a simple command-line interface."""
    service = UserService()

    while True:
        # Check login status to determine menu navigation state
        if not service.current_user:
            print("\n=== Welcome (login/logout Navigation) ===")
            print("1. Register")
            print("2. Login")
            print("3. Forget Password")
            print("4. Exit")
            choice = input("Select an option (1-4): ")
            if choice == "1":
                print("\n--- [Register] ---")
                email = input("Enter Email: ")
                password = input("Enter Password: ")
                name = input("Enter Full Name: ")
                birthdate = input("Enter Birthdate (YYYY-MM-DD): ")
                success, msg = service.register(email, password, name, birthdate)
                print(msg)
            elif choice == "2":
                print("\n--- [Login] ---")
                email = input("Email: ")
                password = input("Password: ")
                success, msg = service.login(email, password)
                print(msg)
            elif choice == "3":
                print("\n--- [Forget Password] ---")
                email = input("Enter registered email: ")
                birthdate = input("Enter registered birthdate (YYYY-MM-DD): ")
                success, msg = service.forget_password_verify(email, birthdate)
                print(msg)
                if success:
                    new_password = input("Enter your new password: ")
                    # Resets password and implicitly finishes [hash password]
                    service.reset_password(email, new_password)
                    print("Password reset successfully!")

            elif choice == "4":
                print("Exiting system. Goodbye!")
                break
            else:
                print("Invalid option, please try again.")
        else:
            # Flowchart Lower Half: Authenticated (Home Page / User Profile)
            user = service.current_user
            print("=== Home Page (Main Information) ===")
            print(f"Logged in as: {user['name']}")
            print("1. View User Profile")
            print("2. Logout")
            choice = input("Select an option (1-2): ")
            if choice == "1":
                print("\n--- User Profile ---")
                print(f"Name: {user['name']}")
                print(f"Email: {user['email']}")
                print(f"Birthdate: {user['birthdate']}")
                print("--------------------")
            elif choice == "2":
                service.logout()
                print("\nLogged out successfully (Remove account session). Returned to main navigation.")
if __name__ == "__main__":
    main()
