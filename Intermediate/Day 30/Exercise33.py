# Instructions

# Issue
# We've got some buggy code. Try running the code. The code will crash and give you an IndexError. This is because we're looking through the list of fruits for an index that is out of range.

# Bad Output
# Error screenshot

# Objective
# Use what you've learnt about exception handling to prevent the program from crashing. If the user enters something that is out of range just print a default output of "Fruit pie".

# Example Input
# ["Apple", "Pear", "Orange"]
# Example Output
#  Fruit pie
# IMPORTANT: The exception handling should NOT allow each fruit to be printed when there is an exeption. e.g. it should not print out Apple pie, Pear pie and Orange pie, when there is an exerception it should only print "Fruit pie".

fruits = eval(input())
# 🚨 Do not change the code above

# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
  try:
    fruit = fruits[index]    
  except IndexError:
    print("Fruit pie")
  else:
    print(fruit + " pie")
# 🚨 Do not change the code below
make_pie(4)