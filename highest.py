students_scores = input("Please enter the score of the students").split(",")
print(students_scores)

for i in range(0, len(students_scores)):
    students_scores[i] = int(students_scores[i])

highest_score = 0
for score in students_scores:
    if score > highest_score:
        highest_score = score
print(f"The Highest score in the class is {highest_score}")
    