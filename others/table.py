from prettytable import PrettyTable


#creating columns for the table
my_file = PrettyTable(["Student's name", "Department", "Program", "Index_number", "Level"])

#creating rows to hold the student information

my_file.add_row(["Dennis", "Computer Science", "PhD", "123456", "Senior"])
my_file.add_row(["Jeremiah", "Mathematics", "Master's", "678901", "Sophomore"])
my_file.add_row(["Sadat", "Physics", "PhD", "234567", "Junior"])

#printing the table
print(my_file)