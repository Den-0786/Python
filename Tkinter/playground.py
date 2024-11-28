def multiply(*args):
    multi = 1
    for num in args:
        if num % 2 == 0:
            multi *= num
    return multi

print(multiply(2, 3, 4, 5, 6))  # should print 240


def add(*args):
    sum = 0
    for n in args:
        if n % 3 == 0:
            sum += n
    return sum

print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # should print 18