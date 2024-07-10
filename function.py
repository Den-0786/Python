
import math
def calc(height, weight, cover):
    number_of_paint = (height * weight)/ cover
    round_up = math.ceil(number_of_paint)
    print(f"You will need {round_up} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
test_c = int(input("Coverage per can: "))
calc(height=test_h, weight=test_w, cover=test_c)

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It is a prime number.")
    else:
        print("It is not a prime number.")
num = int(input("Check this number: "))
prime_checker(number = num)