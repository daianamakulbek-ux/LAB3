# 1. Simple class definition 
class Car:
    def __init__(self, make, model):
        """Constructor to initialize car details."""
        self.make = make
        self.model = model

    def description(self):
        """Returns a description of the car."""
        return f"{self.make} {self.model}"

# 2. Class with a method that returns a greeting
class Person:
    def __init__(self, name, age):
        """Constructor to initialize person's details."""
        self.name = name
        self.age = age

    def greet(self):
        """Returns a greeting message."""
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

# 3. Class with class variables and instance variables
class Dog:
    species = "Canis familiaris"  # Class variable

    def __init__(self, name, breed):
        """Constructor to initialize dog's name and breed."""
        self.name = name  # Instance variable
        self.breed = breed  

# 4. Class with a method for setting and getting attributes
class Employee:
    def __init__(self, name, salary):
        """Constructor to initialize name and salary."""
        self.name = name
        self.salary = salary

    def get_salary(self):
        """Returns the salary of the employee."""
        return self.salary

    def set_salary(self, amount):
        """Sets a new salary for the employee."""
        self.salary = amount

# 5. Class with multiple methods
class Student:
    def __init__(self, name, grade):
        """Constructor to initialize name and grade."""
        self.name = name
        self.grade = grade

    def study(self):
        """Simulates studying."""
        return f"{self.name} is studying."

    def get_grade(self):
        """Returns the grade of the student."""
        return f"{self.name}'s grade is {self.grade}"

car = Car("Toyota", "Corolla")
print(car.description())  # Toyota Corolla

person = Person("Alice", 30)
print(person.greet())  # Hi, I'm Alice and I'm 30 years old.

dog = Dog("Buddy", "Golden Retriever")
print(dog.species)  # Canis familiaris

employee = Employee("John", 50000)
print(employee.get_salary())  # 50000
employee.set_salary(60000)
print(employee.get_salary())  # 60000

student = Student("Bob", "A")
print(student.study())  # Bob is studying.
print(student.get_grade())  # Bob's grade is A
