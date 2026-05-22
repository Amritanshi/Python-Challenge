 # Write a program to find the largest among three entered sales figures.
sales1 = float(input("Enter the first sales figure: "))
sales2 = float(input("Enter the second sales figure: "))
sales3 = float(input("Enter the third sales figure: "))

if sales1 >= sales2 and sales1 >= sales3:
    largest = sales1
elif sales2 >= sales1 and sales2 >= sales3:
    largest = sales2
else:
    largest = sales3

print("The largest sales figure is:", largest)
