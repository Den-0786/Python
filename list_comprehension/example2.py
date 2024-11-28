name = "Dennis"

new_name = [letter for letter in name]
print(new_name)


names = ["Dennis", "Erica", "Owusuaa", "Patricia", 'Judith', "George", "Prince"]

upper_case_names = [name.upper() for name in names if len(name) >= 5]
print(upper_case_names)