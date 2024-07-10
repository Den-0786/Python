numbers = input("Please enter the numbers ").split(",")
print(numbers)

#total = 0
even_sum = 0
#for number in range(0, len(numbers)):
   # numbers[number] = int(numbers[number])
    #total += numbers[number]
    #print(total)
    
for number in range(1, len(numbers) + 1):
    if number % 2 == 0:
        even_sum += number
print(even_sum)