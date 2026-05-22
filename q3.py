# Create a program to check whether a given username and password match predefined credentials. 
username = input("Enter the username: ")
password = input("Enter the password: ")


predefined_username = "admin"
predefined_password = "password123"

if username == predefined_username and password == predefined_password:
    print("Login successful.")
else:
    print("Invalid username or password.")
    