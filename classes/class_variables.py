class Dog:
    # Class variable
    species = "Canis familiaris"  # This is shared by all instances of the class

    def __init__(self, name, breed):
        # Instance variables
        self.name = name
        self.breed = breed

# Creating instances of the Dog class
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Bella", "Bulldog")

# Accessing class variable
print(dog1.species)  # Canis familiaris
print(dog2.species)  # Canis familiaris

# Changing the class variable
Dog.species = "Canis lupus"

# All instances now reflect the updated class variable
print(dog1.species)  # Canis lupus
print(dog2.species)  # Canis lupus
