from user import Admin, Customer

class UserFactory:
    @staticmethod
    def create_user(role, username, password):
        if role == "admin":
            return Admin(username, password)
        elif role == "customer":
            return Customer(username, password)
        else:
            raise ValueError("Invalid role")
