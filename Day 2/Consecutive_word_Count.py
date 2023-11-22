# Problem #2
# Write a program that reads a passage or string and counts the occurrences of two consecutive words 
# that are the same without any other specific word in between.
#  For example, count the occurrences of "apple apple" but not "apple orange apple."
def count_consecutive_words(text):
    words = text.split()
    consecutive_word_count = 0

    for index in range(len(words) - 1):
        if words[index] == words[index + 1]:
            consecutive_word_count += 1

    return consecutive_word_count

passage = input("Enter Your Passage : ")

result = count_consecutive_words(passage)
print(f"Count of the consecutive identical words : {result}")
