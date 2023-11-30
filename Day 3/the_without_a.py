# Problem #2
# Read a passage from a file. 
# Count the number of times the word 'the' followed by another 'the' without 'a' in between.

# Eg The king went to the forest with the wife and a servernt. The king shot a deer. The king went to the forest again the next day.

# answer is 4 (The king, the forest, The King the next).

def count_the_the_pairs(filename): # To define a function count_the_the_pairs with a parameter 
    try:
        # Open the file and read the passage
        with open(filename, 'r+') as file:
            passage = file.read()

        words = passage.lower().split() # Make the passage as lower case and split it into words
        # Initialize count to 0.
        count = 0
        # Set a flag to False to check if the previous word was 'the'.
        previous_was_the = False

        for word in words: # By using stored word and check the condition
            if word == "the": # If word = the means it will be executed
                if previous_was_the: # If true means it will be executed
                    count += 1 # Count increment
                previous_was_the = True 
            elif word == "a": # If word = a means it will be executed
                previous_was_the = False # Set previous_was_the = False

        return count # Return Count
    except Exception as e:
        print(f"An error occurred: {e}")

# Set the filename
filename = "D:\Sayur_Intern\Day 3\passage.txt"

count = count_the_the_pairs(filename) # Calling the function and set the return value on count
    # Print the count.
print("'the' followed by another 'the' without 'a' in between :",count)
