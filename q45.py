#  A railway reservation system wants to verify whether a seat number exists in the reservation list.
# Function to validate mobile no
def validate_mobile(number):
    if number.isdigit() and len(number) == 10:
        print("Valid mobile number")
    else:
        print("Invalid mobile number")

mobile = input("Enter mobile number: ")
validate_mobile(mobile)
