# 1. Using filter() with lambda to get even numbers
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Expected output: [2, 4, 6]

# 2. Using filter() with lambda to get words longer than 5 characters
words = ["apple", "banana", "cherry", "date"]
long_words = list(filter(lambda word: len(word) > 5, words))
print(long_words)  # Expected output: ['banana', 'cherry']

# 3. Using filter() with lambda to get numbers greater than 10
numbers = [5, 10, 15, 20, 25]
greater_than_ten = list(filter(lambda x: x > 10, numbers))
print(greater_than_ten)  # Expected output: [15, 20, 25]

# 4. Using filter() with lambda to get numbers less than 20
less_than_twenty = list(filter(lambda x: x < 20, numbers))
print(less_than_twenty)  # Expected output: [5, 10]

# 5. Using filter() with lambda to get words that contain the letter "a"
filtered_words = list(filter(lambda word: 'a' in word, words))
print(filtered_words)  # Expected output: ['banana', 'cherry']
