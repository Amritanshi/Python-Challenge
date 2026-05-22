# Write a program to split a sentence into words and count total words. 
sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = len(words)
print("Words in the sentence:", words)
print("Total words in the sentence:", word_count)
