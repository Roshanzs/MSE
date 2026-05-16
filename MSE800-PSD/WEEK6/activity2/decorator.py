


def log_activity(func):
    #define the wrapper function to log the activity of the user
    def wrapper(*args, **kwargs):
        print(f"Function: {func.__name__}")
        result = func(*args, **kwargs)
        #检测用户登录状态
        if args:
            zoo = args[0]
            if zoo.user.logged_in:
                print(f"user: {zoo.user.username} already logged in. Performing {func.__name__}")
                return result
            else:
                print("User is not logged in. Please log in to perform this action.")
                return None
        else:
            print("No user information provided. Please log in to perform this action.")
            return None

    return wrapper