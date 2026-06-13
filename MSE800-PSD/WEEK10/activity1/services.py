import hashlib
from datetime import datetime
import database

class UserService:
    def __init__(self):
        # Ensure database and tables are ready when the service starts
        database.init_db()
        self.current_user = None  

    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    @staticmethod
    def validate_date(date_str: str) -> bool:
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def register(self, email: str, password: str, name: str, birthdate: str) -> tuple[bool, str]:
        if not self.validate_date(birthdate):
            return False, "Invalid birthdate format. Please use YYYY-MM-DD."

        # Password hashing
        pwd_hash = self.hash_password(password)
        
        # Save to database
        success = database.insert_user(email, pwd_hash, name, birthdate)
        if success:
            return True, "Account created successfully!"
        else:
            return False, "Registration failed: Email is already registered."

    def login(self, email: str, password: str) -> tuple[bool, str]:
        """Login logic: [login] -> [hash password] -> [Verify hashed password and email]"""
        pwd_hash = self.hash_password(password)
        
        # Verify database entry
        user = database.query_user_by_login(email, pwd_hash)
        
        if user:
            self.current_user = {
                "email": user[0],
                "name": user[1],
                "birthdate": user[2]
            }
            return True, f"Login successful! Welcome back, {user[1]}."
        return False, "Login failed: Incorrect email or password."

    def forget_password_verify(self, email: str, birthdate: str) -> tuple[bool, str]:
        success = database.verify_user_for_reset(email, birthdate)
        if success:
            return True, "Verification successful. You may now reset your password."
        return False, "Verification failed: Email and birthdate do not match our records."

    def reset_password(self, email: str, new_password: str):
        pwd_hash = self.hash_password(new_password)
        database.update_password(email, pwd_hash)

    def logout(self):
        self.current_user = None