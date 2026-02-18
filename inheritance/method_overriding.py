# 1. Method overriding example
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

dog = Dog()
print(dog.speak()) 

# 2. Overriding method with different functionality
class Vehicle:
    def move(self):
        return "Moving forward"

class Car(Vehicle):
    def move(self):
        return "Car is driving"

car = Car()
print(car.move())  # Car is driving

# 3. Overriding method to change the behavior completely
class Animal:
    def move(self):
        return "I move in my own way"

class Fish(Animal):
    def move(self):
        return "I swim in water"

fish = Fish()
print(fish.move())  # I swim in water

# 4. Overriding a method from a parent class and adding extra functionality
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

    def bark_loudly(self):
        return "WOOF WOOF!"

dog = Dog()
print(dog.speak())  # Woof!
print(dog.bark_loudly())  # WOOF WOOF!

# 5. Overriding methods from different parent classes
class A:
    def say_hello(self):
        return "Hello from class A"

class B:
    def say_hello(self):
        return "Hello from class B"

class C(A, B):
    def say_hello(self):
        return super().say_hello() + " and class C!"

c = C()
print(c.say_hello())  # Hello from class A and class C!
