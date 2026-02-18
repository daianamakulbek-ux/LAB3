# 1. Class with __init__ constructor method
class Animal:
    def __init__(self, name, species):
        """Constructor to initialize name and species."""
        self.name = name
        self.species = species

    def get_info(self):
        """Returns the animal's information."""
        return f"{self.name} is a {self.species}"

# 2. Using __init__ to initialize multiple objects
class Book:
    def __init__(self, title, author):
        """Constructor to initialize book details."""
        self.title = title
        self.author = author

    def info(self):
        """Returns book's title and author."""
        return f"'{self.title}' by {self.author}"

# 3. Using __init__ to initialize default values
class House:
    def __init__(self, address, color="White"):
        """Constructor with default color."""
        self.address = address
        self.color = color

    def get_details(self):
        """Returns the house details."""
        return f"The house at {self.address} is {self.color}."

# 4. __init__ with multiple attributes
class Movie:
    def __init__(self, title, year, director):
        """Constructor to initialize movie details."""
        self.title = title
        self.year = year
        self.director = director

    def movie_info(self):
        """Returns the movie information."""
        return f"{self.title} ({self.year}), directed by {self.director}"

# 5. __init__ with instance variables and a method
class Car:
    def __init__(self, make, model, year):
        """Constructor to initialize car details."""
        self.make = make
        self.model = model
        self.year = year

    def car_info(self):
        """Returns the car's information."""
        return f"{self.year} {self.make} {self.model}"

animal = Animal("Lion", "Mammal")
print(animal.get_info())  # Lion is a Mammal

book = Book("1984", "George Orwell")
print(book.info())  # '1984' by George Orwell

house = House("123 Elm St")
print(house.get_details())  # The house at 123 Elm St is White.

movie = Movie("Inception", 2010, "Christopher Nolan")
print(movie.movie_info())  # Inception (2010), directed by Christopher Nolan

car = Car("Tesla", "Model S", 2020)
print(car.car_info())  # 2020 Tesla Model S
