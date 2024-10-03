
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        print("Cannot divide by zero")
        return
    else:
        return num1 / num2
    
def modulo(num1, num2):
    return num1 % num2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": modulo
}

def calculate():
    num1 = float(input("Enter the first number: \n"))
    operation = input("Enter the operator (+, -, *, /, %): \n")
    if operation not in operations:
        print("Invalid operator. Please use one of the following: +, -, *, /, %")
        return
    num2 = float(input("Enter the second number: \n"))
    
    results = operations[operation](num1, num2)
    if results is not None:
        print(f"Answer: {results}")
        
is_on = True
while is_on:
    calculate()
    is_on = input("Do you want to perform another calculation? (yes/no) \n").lower() == "yes"
    