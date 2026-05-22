#  A bank wants to calculate simple interest for customers based on principal, rate, and time entered by the user. 

p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest (in %): "))
t = float(input("Enter the time (in years): "))

si = (p * r * t) / 100
print("Simple interest:", si)