
def calculate_basic(x, y):
    plus = x + y
    print(f"x + y = {plus}")
    minus = x - y
    print(f"x - y = {minus}")

def calculate_advanced(x, y):
    times = x * y
    print(f"x * y = {times}")
    if y != 0:
        divide = x / y
        print(f"x / y = {divide}")
    else:
        print("Cannot divide by zero.")

def calculate_modulo(x, y):
    left = x % y
    print(f"x % y = {left}")


if __name__ == "__main__":
    x = input("Enter the value of x: ")
    y = input("Enter the value of y: ")
    x = int(x)
    y = int(y)
    calculate_basic(x, y)
    calculate_advanced(x, y)
    calculate_modulo(x, y)


    