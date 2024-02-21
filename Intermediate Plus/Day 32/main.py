##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import pandas
import random

MY_EMAIL = "zbindasilva@gmail.com"
MY_PASSWORD = "qede srib ebtl pykt"

birth_csv = pandas.read_csv("./birthdays.csv")
birth_dict = birth_csv.to_dict("records")

date_now = dt.datetime.now()
current_month = date_now.month
current_day = date_now.day

for person in birth_dict:
    if person["month"] == current_month and person["day"] == current_day:
        letter_number = random.randint(1,3)
        with open(f"./letter_templates/letter_{letter_number}.txt") as letter_file:
            letter = letter_file.read()
            new_letter = letter.replace("[NAME]", person["name"])
        
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(        
                from_addr=MY_EMAIL,
                to_addrs="zbindeoliveira@yahoo.com",
                msg=f"Subject:Happy Birthday!!\n\n{new_letter}"
            )


