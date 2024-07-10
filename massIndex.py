# calculating body mass index 
height = input("enter the height in m:")
weight = input("enter the weight in kg:")
bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
new_bmi = str(bmi_as_int)
print("Your bmi is " + new_bmi)