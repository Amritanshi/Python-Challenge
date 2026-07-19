#  A grocery shop owner wants to calculate the final bill after applying discounts based on the purchase amount. 
# Write a program using if...elif...else to display the final amount. 
purchase_amount = float(input("Enter the purchase amount: "))

if purchase_amount >= 1000:
    discount = 0.2
elif purchase_amount >= 500:
    discount = 0.1
else:
    discount = 0

final_amount = purchase_amount - (purchase_amount * discount)
print("Final amount after discount:", final_amount)
