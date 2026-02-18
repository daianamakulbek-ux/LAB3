# 1. Function that returns the square of a number
def square(x):
    """Returns the square of a number."""
    return x ** 2
    print(square(4))

# 2. Function that returns the minimum and maximum of a list
def get_min_max(numbers):
    """Returns the minimum and maximum of a list."""
    return min(numbers), max(numbers)
    min_val, max_val = get_min_max([1, 5, 3, 9, 7])
      print(f"Min: {min_val}, Max: {max_val}")

# 3. Function that returns multiple values
def get_full_name(first_name, last_name):
    """Returns the full name."""
    return first_name + " " + last_name
      print(get_full_name("John", "Doe"))
   

# 4. Function that returns a greeting
def greet(name):
    """Greets the user."""
    return f"Hello, {name}!"
    print(greet("Alice"))

# 5. Function that returns a boolean value
def is_even(n):
    """Checks if a number is even."""
    return n % 2 == 0
    print(is_even(4))
  


