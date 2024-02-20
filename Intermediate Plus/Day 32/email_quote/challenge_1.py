import smtplib
import datetime as dt
import random

with open("./quotes.txt", "r") as quotes_file:
    quotes = quotes_file.readlines()

current_day = dt.datetime.now()
week_day = dt.datetime.weekday(current_day)

if week_day == 1:
    random_quote = random.choice(quotes)
    my_email = "zbindasilva@gmail.com"
    password = "qede srib ebtl pykt"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(        
            from_addr=my_email,
            to_addrs="zbindeoliveira@yahoo.com",
            msg=f"Subject:A Quote to make your day better!!\n\n{random_quote}"
        )

