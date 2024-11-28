
#with comprehension
# creating the list of numbers
#numbers = [2,4,6]

# using list comprehension to multiply 2 to each number
#new_list = [n * 2 for n in numbers ]
#print(new_list)



range_list = [n * 2 for n in range(1,100) if n % 2 == 0]

even_numbers = range_list
print(even_numbers)

# summing up the numbers in the list
sum_even_numbers = sum(even_numbers)
print(sum_even_numbers)