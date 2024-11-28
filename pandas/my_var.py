import pandas

data = pandas.read_csv("pandas/census.csv")

#get the data of the various squirrel type
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"] )
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
white_squirrels_count = len(data[data["Primary Fur Color"] == "White"])

print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)
print(white_squirrels_count)


data_dict = {
    "Fur Color": ["gray", "red", "black", "white"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count, white_squirrels_count]
}

squirrel_data = pandas.DataFrame(data_dict)
print(squirrel_data)

squirrel_data.to_csv("squirrel.csv")