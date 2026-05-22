
# Write a program to read names from a file and display them in sorted order. 
with open("names.txt", "r") as file:
    names = file.read().splitlines()

names.sort()

print("Sorted names:")
for name in names:
    print(name)
