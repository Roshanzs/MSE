
## Project Structure

- `main.py`: Entry point of the program. Demonstrates the use of decorators and user/zoo functionality.
- `decorator.py`: Contains the implementation of the decorator used in the project.
- `user.py`: Defines the `User` class and related user functionality.
- `zoo.py`: Contains the `Zoo` class and related zoo management logic.

## Functionality

This project demonstrates the use of Python decorators to add additional behavior to functions or methods. The main focus is on how decorators can be used to modify or enhance the behavior of class methods, such as logging, access control, or other cross-cutting concerns.

- Users can interact with the zoo system, performing actions that are managed and possibly modified by decorators.
- The code is organized for clarity, separating concerns into different modules.

## Decorator Implementation

The decorator is implemented in `decorator.py`. It wraps target functions or methods to add extra functionality (such as logging or validation) before or after the original function executes. The decorator is applied using the `@log_activity` syntax above the function definition.

Example usage:

```python
from decorator import log_activity

@log_activity
def some_function():
    # function logic
```

This approach allows for clean, reusable, and maintainable code by separating additional behavior from core logic.
