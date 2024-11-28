def fibonacciGenerator(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
        yield fib_sequence[i]
    print(fib_sequence)

for num in fibonacciGenerator(20):
    print(num)