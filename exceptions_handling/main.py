#FileNotFound  
try:
    file = open("exceptions_handling/my_name.txt")
    a_dictionary = {"key": "value"}
    open(a_dictionary["key"])
    
except FileNotFoundError:
    file = open("exceptions_handling/my_name.txt", "w")
    file.write("My Name Is Dennis Opoku Amponsah")
    
except KeyError as error_message:
    print(f"The dictionary does not contain the key {error_message}")
else:
    content = file.read() 
    print(content)