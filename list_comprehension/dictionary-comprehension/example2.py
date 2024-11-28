student_dict = {
    "Student" : ["Angela", "Samuel", "Noah", "John", "Elijah", "Elisha", "David", "Jonathan"],
    "score" : [89, 92, 78, 96, 82, 91, 85, 97]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)

#average_score = student_data_frame["score"].mean()
#print(average_score)

for (index, row) in student_data_frame.iterrows():
    name = row["Student"]
    score = row["score"]
    print(f"{name}: {score}")