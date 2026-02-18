# 1.function that returns a greeting with a name
def greet(name):
    """Returns a greeting with the given name."""
    return f"Hello, {name}!"
    print(greet("Alice"))
# 2. Function with no parameters that returns a simple greeting
def say_hello():
    """Just says 'Hello!'."""
    return "Hello!"
    print(say_hello())

# 3. Function that returns the sum of two numbers
def add(a, b):
    """Adds two numbers."""
    return a + b
    print(add(5, 3))

# 4. Function that returns the product of a list of numbers
def multiply_list(numbers):
    """Returns the product of the numbers in a list."""
    result = 1
    for num in numbers:
        result *= num
    return result
    print(multiply_list([1, 2, 3, 4]))

# 5. Function that returns the square of a number
def square(x):
    """Returns the square of a number."""
    return x ** 2
    print(square(4))



