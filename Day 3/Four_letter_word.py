# Problem #3
# From the same file as above, read from the file, count the number of unique 4 letter words and it no of occurrences
# for each word. Write this information at the end of file under the heading "Summary of 4 letter words"
# Function to count 4-letter words and their occurrences
def count_4_letter_words(file_content):
    words = file_content.split()
    word_count = {}

    for word in words:
        if len(word) == 4:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    return word_count

# Read the contents of the file
file_path = 'D:\Sayur_Intern\Day 3\passage.txt'  # Replace with your file path
with open(file_path, 'r') as file:
    content = file.read()

    # Count unique 4-letter words and their occurrences
    words_and_counts = count_4_letter_words(content)

    # Calculate the total number of unique 4-letter words
    total_unique_words = len(words_and_counts)

    # Append the summary to the file
    print("\n\nSummary of 4 letter words\n")
    print("--------------------------\n")
    print(f"Total unique 4-letter words: {total_unique_words}\n")

    # Write occurrences of each word
    for word, count in words_and_counts.items():
        print(f"{word}: {count} occurrences\n")
