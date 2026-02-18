# 1. Positional arguments
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b
    print(add(5, 3))
   

# 2. Default argument
def greet(name="Guest"):
    """Greets the user."""
    return f"Hello, {name}!"
    print(greet())

# 3. *args for an arbitrary number of positional arguments
def sum_numbers(*args):
    """Returns the sum of all numbers passed to the function."""
    return sum(args)
    print(sum_numbers(1, 2, 3, 4))

# 4. **kwargs for an arbitrary number of keyword arguments
def print_person_info(**kwargs):
    """Prints information about a person."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        print_person_info(name="Alice", age=25)

# 5. Function with default arguments and multiple parameters
def power_of(base, exponent=2):
    """Raises the base to the given exponent."""
    return base ** exponent
    print(power_of(3))


