import random

#Treasure Map
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
try:
    letter = position[0].lower()
    abc = ["a", "b", "c"]
    
    if letter not in abc:
        raise ValueError("Invalid column letter")
    
    letter_index = abc.index(letter)
    number_index = int(position[1]) - 1
    if number_index < 0 or number_index > 2:
        raise ValueError("Invalid row number")
    
    map[number_index][letter_index] = "X"

    for row in map:
        print(''.join(row))
#Write your code above this row 👆
except(IndexError, ValueError) as e:
    print(f"Error: {e}. Please enter a valid position in the format 'a0', 'b1', 'c2' etc.")
# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")