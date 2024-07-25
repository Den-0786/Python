# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
# my_screen = Screen()

# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Student Name", ["Dennis Opoku Amponsah", "Eva Owusuaa Amponsem", "Erica Serwaa Amoako", "Isaac Owusu Francis", "Emmanuel Fosu Ebenezer"])
table.add_column("Department", ["Computer Science", "Biological Science", "Chemical Science", "Physics", "Mathematics"])
table.add_column("Student Gender", ["Male", "Female", "Female", "Male", "Male"])
table.add_column("Student Marks", [80, 70, 90, 80, 70])
table.add_column("Student Grade", ["A", "B", "A", "A", "B"])

table.align = "l"

print(table)