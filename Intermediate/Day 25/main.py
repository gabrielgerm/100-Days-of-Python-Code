# import csv

# with open("weather_data.csv") as data_file:
#     csv_data = csv.reader(data_file)
#     temperature_list = []
#     for row in csv_data:
#         temperature_list.append(int(row[1]))
# print(temperature_list)

import pandas

data = pandas.read_csv("weather_data.csv")
temp_list = data["temp"]

print(temp_list.mean())
print(temp_list.max())