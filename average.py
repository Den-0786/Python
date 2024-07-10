

student_heights =input("Please enter the height of the students separated by a comma: ").split(",")
print(student_heights)
total_height = 0
for height in student_heights:
    height = int(height)
    total_height += height
print(f"Total height = {total_height}")


number_of_students = 0
for students in student_heights:
    number_of_students += 1
print(f"Number_of_students = {number_of_students}")

Average_height = round(total_height / number_of_students)
print(f"Average_height = {Average_height}")