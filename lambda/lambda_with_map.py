# 1. Using lambda with map() to square numbers
numbers = [1, 2, 3, 4]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Expected output: [1, 4, 9, 16]

# 2. Using lambda with map() to double numbers
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)  # Expected output: [2, 4, 6, 8]

# 3. Using lambda with map() to capitalize words
words = ["apple", "banana", "cherry"]
capitalized_words = list(map(lambda word: word.capitalize(), words))
print(capitalized_words)  # Expected output: ['Apple', 'Banana', 'Cherry']

# 4. Using lambda with map() to get the length of words
word_lengths = list(map(lambda word: len(word), words))
print(word_lengths)  # Expected output: [5, 6, 6]

# 5. Using lambda with map() to filter out None values
filtered_words = list(map(lambda word: word if len(word) > 5 else None, words))
print(filtered_words)  # Expected output: [None, 'banana', 'cherry']
