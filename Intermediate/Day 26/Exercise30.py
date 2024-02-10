# Instructions
# 💪 This exercise is HARD
# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.

# You are going to create a list called result which contains the numbers that are common in both files.

# e.g. if file1.txt contained:

# 1
# 2
# 3
# and file2.txt contained:

# 2
# 3
# 4
# result = [2, 3]
# IMPORTANT: The output should be a list of integers and not strings! Try to use List Comprehension instead of a Loop.

# Example Output
# [3, 6, 5, 33, 12, 7, 42, 13]

with open("file1.txt") as f1:
    file1_numbers = f1.readlines()

with open("file2.txt") as f2:
    file2_numbers = f2.readlines()

result = [int(num) for num in file1_numbers if num in file2_numbers]


# Write your code above 👆
print(result)
