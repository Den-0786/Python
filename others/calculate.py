
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


def calculate(previous_result = None):
    if previous_result is not None:
        print(f"Previous answer = : {previous_result}")
        num1 = previous_result
    else:
        num1 = float(input("Enter the first number: \n"))
        
    operation = input("Enter the operator (+, -, *, /, %): \n")
    if operation not in operations:
        print("Invalid operator. Please use one of the following: +, -, *, /, %")
        return None
    
    num2 = float(input("Enter the second number: \n"))
    
    results = operations[operation](num1, num2)
    if results is not None:
        print(f"Answer: {results}")
        return results
    return previous_result
        
is_on = True
previous_results = None
while is_on:
    previous_results = calculate(previous_results)
    new_input = input("Do you want to perform another calculation? (yes/no) \n").lower()
    if new_input == "yes":
        another = input("Do you want to continue from the previous calculation? (yes/no) \n").lower()
        if another == "no":
            previous_results = None
    elif new_input == "no":
        is_on = False
        print("Thank you for using the calculator. Goodbye!")