#Instructions

'''Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Equal to or over 25 but below 30 they are slightly overweight
Equal to or over 30 but below 35 they are obese
Equal to or over 35 they are clinically obese.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m)'''


# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi_number = weight/height**2
if bmi_number < 18.5:
  print(f"Your BMI is {bmi_number}, you are underweight.")
elif bmi_number > 18.5 and bmi_number < 25:
  print(f"Your BMI is {bmi_number}, you have a normal weight.")
elif bmi_number >= 25 and bmi_number < 30:
  print(f"Your BMI is {bmi_number}, you are slightly overweight.")
elif bmi_number >= 30 and bmi_number < 35:
  print(f"Your BMI is {bmi_number}, you are obese.")
else:
  print(f"Your BMI is {bmi_number}, you are clinically obese.")