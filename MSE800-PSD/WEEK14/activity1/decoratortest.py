
# Describe the demo: registering decorated objects in an application-level map.
# Registering decorated objects to an AP

# Enable Python 3 style print(...) behavior in Python 2.x environments.
from __future__ import print_function # 2.X

# Create a global registry that maps object names to function/class objects.
registry = {}

# Define a decorator that can decorate both functions and classes.
def register(obj):                          # Both class and func decorator
    # Store the object in the registry using its __name__ as the key.
    registry[obj.__name__] = obj            # Add to registry
    # Return the original object (no wrapper), so call behavior is unchanged.
    return obj                              # Return obj itself, not a wrapper

# Apply register to spam (equivalent to: spam = register(spam)).
@register
# Define a function that returns x squared.
def spam(x):
    # Compute and return x^2.
    return(x ** 2)                          # spam = register(spam)

# Apply register to ham (equivalent to: ham = register(ham)).
@register
# Define a function that returns x cubed.
def ham(x):
    # Compute and return x^3.
    return(x ** 3)

# Apply register to class Eggs (equivalent to: Eggs = register(Eggs)).
@register
# Define a class whose value is x to the fourth power.
class Eggs:                                 # Eggs = register(Eggs)
    # Initialize an instance with x^4 stored in self.data.
    def __init__(self, x):
        # Save x^4 in an instance attribute.
        self.data = x ** 4

    # Define string representation for printing Eggs instances.
    def __str__(self):
        # Return self.data as a string.
        return str(self.data)

# Print a heading before listing registry content.
print('Registry:')

# Iterate through each registered object name.
for name in registry:
    # Print name, object reference, and the object's type.
    print(name, '=>', registry[name], type(registry[name]))

# Print a heading for direct/manual calls.
print('\nManual calls:')

# Call spam directly with argument 2.
print(spam(2))
# Call ham directly with argument 2.
print(ham(2))
# Instantiate Eggs directly with argument 2.
X = Eggs(2)
# Print the Eggs instance (uses __str__).
print(X)

# Print a heading for calls made via the registry.
print('\nRegistry calls:')

# Iterate through each registered object name again.
for name in registry:
    # Call each registered object with argument 2 and print the result.
    print(name, '=>', registry[name](2))    # Invoke from registry

# Brief summary of Python decorators:
# - Purpose: Decorators let you reuse cross-cutting behavior (e.g., registration,
#   logging, timing, validation, caching) without rewriting core function/class code.
# - How they work: @decorator is syntax sugar for reassignment:
#   target = decorator(target). A decorator may return the same target or a wrapper.
# - Extending this code: You can return wrappers to intercept calls, build
#   parameterized decorators (decorator factories), store extra metadata in
#   registry, or use functools.wraps to preserve wrapped-function metadata.