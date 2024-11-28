names =  ["Erica", "Owusuaa", "Patricia", 'Judith',"Dennis", "George", "Prince"]

import random

student_score = {students: random.randint(1, 100) for students in names}

passed_scores =  {student: score for (student, score) in student_score.items() if score >= 60}
print(passed_scores)