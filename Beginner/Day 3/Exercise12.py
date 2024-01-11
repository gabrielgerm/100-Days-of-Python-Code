#Instructions

'''
💪 This is a difficult challenge! 💪
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs.

Then check for the number of times the letters in the word LOVE occurs.

Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is *x*, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:

"Your score is *y*, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is *z*."'''


print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
total_true=0
total_love=0
two_names = (name1 + name2).lower()

total_true += two_names.count("t")
total_true += two_names.count("r")
total_true += two_names.count("u")
total_true += two_names.count("e")

total_love += two_names.count("l")
total_love += two_names.count("o")
total_love += two_names.count("v")
total_love += two_names.count("e")

love_score = int(str(total_true) + str(total_love))

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
   print(f"Your score is {love_score}.")