#Instructions

'''This is a difficult challenge. 💪

You are going to write a program that will mark a spot on a map with an X.

In the starting code, you will find a variable called map.

This map contains a nested list. When map is printed this is what it looks like, notice the nesting:

[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{row1}\n{row2}\n{row3}") to format the 3 lists to be printed as a 3 by 3 grid, each on a new line.

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']'''


line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
if position[1] == "1":
  if position[0] == "A":
    line1[0] = "X"
  elif position[0] == "B":
    line1[1] = "X"
  else:
    line1[2] = "X"
elif position[1] == "2":
  if position[0] == "A":
    line2[0] = "X"
  elif position[0] == "B":
    line2[1] = "X"
  else:
    line2[2] = "X"
else:
  if position[0] == "A":
    line3[0] = "X"
  elif position[0] == "B":
    line3[1] = "X"
  else:
    line3[2] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")