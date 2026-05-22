#  A movie theatre wants to assign ticket pricing based on age categories such as child, adult, and senior citizen.
age = int(input("Enter the age of the person: "))

if age < 13:
    ticketprice = 10
elif 13 <= age <= 65:
    ticketprice = 20
else:
    ticketprice = 15

print("Ticket price:", ticketprice)