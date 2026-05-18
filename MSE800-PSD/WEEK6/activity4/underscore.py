

# 1. As a loop variable name for unused values
for _ in range(5):
    print("This will be printed 5 times.")

# 2. As a placeholder for the last evaluated expression in the interactive shell
a = 2 + 3
_ = a
print(_)  # Output: 5

# 3. As a separator in numeric literals for better readability
number = 1_000_000
print(number)  # Output: 1000000   

# 4. ignoring unused variables in unpacking
x, _, y = (1, 2, 3)
print(x)  # Output: 1
print(y)  # Output: 3

# 5. As a convention for "don't care" variables in function definitions
def my_function(a, _, c):
    return a + c
