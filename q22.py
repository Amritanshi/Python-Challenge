# Write a program to reverse each word in a given sentence

sentence = input("Enter a sentence: ")
words = sentence.split()

reversed_words = [word[::-1] for word in words]

result = " ".join(reversed_words)

print("Sentence with each word reversed:")
print(result)



