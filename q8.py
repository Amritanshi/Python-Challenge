# A school wants to calculate grades for students based on marks obtained in five subjects. 
marks1 = float(input("Enter marks for subject 1: "))
marks2 = float(input("Enter marks for subject 2: "))
marks3 = float(input("Enter marks for subject 3: "))
marks4 = float(input("Enter marks for subject 4: "))
marks5 = float(input("Enter marks for subject 5: "))

totalmarks = marks1 + marks2 + marks3 + marks4 + marks5
averagemarks = totalmarks / 5

if averagemarks >= 90:
    grade = "A+"
elif averagemarks >= 80:
    grade = "A"
else:
    grade = "B"

print("Total marks:", totalmarks)
print("Average marks:", averagemarks)
print("Grade:", grade)