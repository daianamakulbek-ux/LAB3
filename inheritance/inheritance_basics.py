# 1. Basic inheritance example
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

dog = Dog()
print(dog.speak())  # Expected output: Woof!

# 2. Inheritance with shared attributes
class Person:
    def __init__(self, name, age):
        """Constructor to initialize name and age."""
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)  # Call the parent constructor
        self.salary = salary

employee = Employee("Alice", 30, 50000)
print(employee.name)  # Alice
print(employee.salary)  # 50000

# 3. Inheritance with method call
class Animal:
    def move(self):
        return "Moving"

class Bird(Animal):
    def move(self):
        return "Flying"

bird = Bird()
print(bird.move()) 

# 4. Inheriting from a class without modifying behavior
class Vehicle:
    def honk(self):
        return "Beep beep"

class Car(Vehicle):
    pass  # Inheriting without modifying the behavior

car = Car()
print(car.honk()) 

# 5. Multiple levels of inheritance
class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def bark(self):
        return "Woof!"

class Puppy(Dog):
    def play(self):
        return "Puppy is playing"

puppy = Puppy()
print(puppy.sound())  
print(puppy.bark()) 
print(puppy.play())  
