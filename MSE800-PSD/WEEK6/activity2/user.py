
from decorator import log_activity

defultUsername = "user1"
defultPassword = "password123"

class User:
    def __init__(self, username, password):
        if username:
            self.username = username
        else:
            self.username = defultUsername
        if password:
            self.password = password
        else:
            self.password = defultPassword
        self.logged_in = False

def userLogin(username, password):
    if defultUsername == username and defultPassword == password:
        user = User(username, password)
        user.logged_in = True
        print(f"{username} has logged in.")
        return user
    else:
        print("Invalid username or password.")
        return None


def userLogout(user):
    if user and user.logged_in:
        user.logged_in = False
        print(f"{user.username} has logged out.")