#  A company wants to identify whether an employee is eligible for a bonus based on attendance percentage and 
# performance rating.
attendance_percentage = float(input("Enter the attendance percentage: "))
performance_rating = float(input("Enter the performance rating (1-5): "))

if attendance_percentage >= 80 and performance_rating >= 4:
    print("Employee is eligible for a bonus.")
else:
    print("Employee is not eligible for a bonus.")