# 1. Using *args for an arbitrary number of positional arguments
def greet_multiple(*names):
    """Greets multiple people."""
    for name in names:
        print(f"Hello, {name}!")
        greet_multiple("Alice", "Bob", "Charlie")

# 2. Using **kwargs for an arbitrary number of keyword arguments
def print_details(**details):
    """Prints all details as key-value pairs."""
    for key, value in details.items():
        print(f"{key}: {value}")
        print_details(name="John", age=30)

# 3. Function that sums all the numbers passed
def sum_numbers(*args):
    """Sums all the numbers passed."""
    return sum(args)
    print(sum_numbers(1, 2, 3, 4))


# 4. Function with default arguments and arbitrary parameters
def power_of(base, exponent=2):
    """Raises a number to a power."""
    return base ** exponent
    print(power_of(3))

# 5. Function with multiple parameters
def display_info(name, age, **kwargs):
    """Displays info about a person."""
    print(f"Name: {name}, Age: {age}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        display_info("Alice", 25, country="USA", city="New York")

