# Problem #1
# write a program that reads a passage and reverses the order of 
# letters in each word while keeping the word order intact. Use function.
# Eg- input - I am Sayur
# Output I ma ruyaS

sentences = input("Enter Your sentences : ")

sentences = sentences.split()

for word in sentences :
    print(word[::-1],end=" ")
    