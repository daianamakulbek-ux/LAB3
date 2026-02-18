# 1. Using lambda with sorted() to sort numbers
numbers = [3, 1, 4, 2]
sorted_numbers = sorted(numbers, key=lambda x: x)
print(sorted_numbers)  # Expected output: [1, 2, 3, 4]

# 2. Using lambda with sorted() to sort words by length
words = ["apple", "banana", "cherry"]
sorted_by_length = sorted(words, key=lambda word: len(word))
print(sorted_by_length)  # Expected output: ['apple', 'cherry', 'banana']

# 3. Using lambda with sorted() to sort numbers in descending order
sorted_numbers_desc = sorted(numbers, key=lambda x: x, reverse=True)
print(sorted_numbers_desc)  # Expected output: [4, 3, 2, 1]

# 4. Using lambda with sorted() to sort words by the first letter
sorted_words = sorted(words, key=lambda word: word[0])
print(sorted_words)  # Expected output: ['apple', 'banana', 'cherry']

# 5. Using lambda with sorted() to sort tuples by the second value
pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # Expected output: [(1, 'one'), (2, 'two'), (3, 'three')]
