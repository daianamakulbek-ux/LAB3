# 1. Using super() to call parent methods
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Calls the parent constructor
        self.breed = breed

    def speak(self):
        return super().speak() + " Woof!"

dog = Dog("Buddy", "Golden Retriever")
print(dog.speak())  # Buddy makes a sound. Woof!

# 2. Using super() to access parent methods in multiple inheritance
class A:
    def greet(self):
        return "Hello from class A"

class B:
    def greet(self):
        return "Hello from class B"

class C(A, B):
    def greet(self):
        return super().greet() + " and class C!"

c = C()
print(c.greet())  # Hello from class A and class C!

# 3. Calling a parent method with multiple levels of inheritance
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def description(self):
        return f"This is a vehicle of brand {self.brand}."

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def description(self):
        return super().description() + f" Model: {self.model}"

car = Car("Toyota", "Camry")
print(car.description())  # This is a vehicle of brand Toyota. Model: Camry

# 4. Using super() to call parent method in constructor
class Animal:
    def __init__(self, species):
        self.species = species

class Dog(Animal):
    def __init__(self, species, name):
        super().__init__(species)  # Calls the parent constructor
        self.name = name

    def show_info(self):
        return f"{self.name} is a {self.species}"

dog = Dog("Golden Retriever", "Max")
print(dog.show_info())  # Max is a Golden Retriever

# 5. Using super() to avoid calling the same method from parent multiple times
class A:
    def info(self):
        return "Info from A"

class B(A):
    def info(self):
        return super().info() + " and B"

b = B()
print(b.info())  # Info from A and B
