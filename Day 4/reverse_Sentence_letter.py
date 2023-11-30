# Problem #1
# write a program that reads a passage and reverses the order of 
# letters in each word while keeping the word order intact. Use function.
# Eg- input - I am Sayur
# Output I ma ruyaS

def Reversing_Sentence_words(sentence):
    sentence = sentence.split()
    for word in sentence :
        print(word[::-1],end=" ")


sentence = input("Enter Your sentences : ")

Reversing_Sentence_words(sentence)


    