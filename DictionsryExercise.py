def score_to_grade(score):
    if score > 90:
        return "A"
    elif score > 80:
        return "B"
    elif score > 70:
        return "C"
    elif score > 60:
        return "D"
    else:
        return "F"


Student_score ={
    "Harry":81,
    "Ron":78,
    "Dennis":99,
    "Draco":74,
    "Neville":62,
}


student_grades = {}

student_grades = {student:score_to_grade(score) for student, score in Student_score.items()}
print(student_grades)

#for student in Student_score:
    
    #score = Student_score[student]
    
    #if score > 90:
        # student_grades[student] = "Outstanding"
    #elif score > 80:
        #student_grades[student] = "Exceeds Expectations"
    #elif score > 70:
        # student_grades[student] = "Acceptable"
    #else:
        #student_grades[student] = "Fail"
        
#print(student_grades)
