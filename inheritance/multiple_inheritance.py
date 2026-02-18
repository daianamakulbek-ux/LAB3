# 1. Basic example of multiple inheritance
class Animal:
    def speak(self):
        return "Animal sound"

class Bird:
    def fly(self):
        return "Flying"

class Parrot(Animal, Bird):
    pass

parrot = Parrot()
print(parrot.speak())  # Animal sound
print(parrot.fly())  # Flying

# 2. Multiple inheritance with method overriding
class Animal:
    def speak(self):
        return "Animal sound"

class Dog:
    def bark(self):
        return "Woof!"

class Puppy(Dog, Animal):
    def speak(self):
        return super().speak() + " Woof!"

puppy = Puppy()
print(puppy.speak())  # Animal sound Woof!
print(puppy.bark())  # Woof!

# 3. Multiple inheritance with calling different parent methods
class A:
    def speak(self):
        return "Speaking from A"

class B:
    def speak(self):
        return "Speaking from B"

class C(A, B):
    def speak(self):
        return A.speak(self) + " and " + B.speak(self)

c = C()
print(c.speak())  # Speaking from A and Speaking from B

# 4. Multiple inheritance with shared class variables
class Parent1:
    species = "Human"

class Parent2:
    country = "USA"

class Child(Parent1, Parent2):
    pass

child = Child()
print(child.species)  # Human
print(child.country)  # USA

# 5. Multiple inheritance with calling `super()` for the parent methods
class A:
    def speak(self):
        return "Speaking from class A"

class B:
    def speak(self):
        return "Speaking from class B"

class C(A, B):
    def speak(self):
        return super().speak() + " and class C!"

c = C()
print(c.speak())  # Speaking from class A and class C!
