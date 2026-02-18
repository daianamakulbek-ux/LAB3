# 1. Class with instance methods
class Dog:
    def __init__(self, name, breed):
        """Constructor to initialize name and breed."""
        self.name = name
        self.breed = breed

    def bark(self):
        """Simulates the dog's barking."""
        return f"{self.name} says woof!"

# 2. Class with a method that updates attributes
class Cat:
    def __init__(self, name, age):
        """Constructor to initialize name and age."""
        self.name = name
        self.age = age

    def grow(self):
        """
