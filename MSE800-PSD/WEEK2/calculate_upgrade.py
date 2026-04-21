# define a class to calculate basic and advanced operations
class calculate:
    def calculate_basic(self, x, y):
        plus = x + y
        minus = x - y
        return f"x + y = {plus}, x - y = {minus}"

    def calculate_advanced(self, x, y):
        times = x * y
        if y != 0:
            divide = x / y
        else:
            divide = "undefined"
        return f"x * y = {times}, x / y = {divide}"
    
    def calculate_modulo(self, x, y):
        left = x % y
        return f"x % y = {left}"

# functions to get arguments
def getArgument():
    x = input("Enter the value of x: ")
    return int(x)

# function to print results
def printResults(res):
    for result in res:
        print(result)

if __name__ == "__main__":
    x = getArgument()
    y = getArgument()
    calc = calculate()
    results = [
        calc.calculate_basic(x, y),
        calc.calculate_advanced(x, y),
        calc.calculate_modulo(x, y)
    ]
    printResults(results)