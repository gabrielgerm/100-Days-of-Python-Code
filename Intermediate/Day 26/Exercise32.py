# Instructions
# You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.

# To convert temp_c into temp_f use this formula:

# (temp_c * 9/5) + 32 = temp_f
# Celsius to Fahrenheit chart

# Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.

# The eval() function will help us convert the string input into a Python dictionary, provided that the inputs are already formatted with the correct syntax.

weather_c = eval(input())
# 🚨 Don't change code above 👆

# Write your code 👇 below:
weather_f = {day:(temperature * 9/5) + 32 for (day, temperature) in weather_c.items()}


print(weather_f)