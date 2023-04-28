# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#

# import pandas

# data = pandas.read_csv("weather_data.csv")
# avg_temp = data["temp"].mean()
# # max_temp = data["temp"].max()
# max_temp = data.temp.max()
# print(f"Average temperature: {avg_temp}")
# print(f"Maximum temperature: {max_temp}")
# print(data[data.day == "Monday"])
# print(type(data))
# print(data["temp"])
# print(type(data["temp"]))
# print("Hottest day:")
# print(data[data.temp == data.temp.max()])
#
# # Create dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
df = pandas.DataFrame(data_dict)
print(df)
df.to_csv("squirrels_count.csv")
