# Generate the following output using for loop. Go until g.
# a
# aba
# abacaba
# abacabadabacaba
# abacabadabacabaeabacabadabacaba

# look at the output and find the pattern. Hint - add next letter in the alphabet in each row
Start_char = input("Enter the starting letter you need : ")    # asking user to type what character should begins

Start_char = ord(Start_char)  # converting it into number

front_back=total_str=""   # initializing two string varriable

rows = int(input("Enter the number of rows you need : "))   # asking number of rows

for row in range(1,rows+1): # to traverse the rows
    total_str = front_back+chr(Start_char)+front_back  # adding front_back + input letter + front_back
    print(total_str)    # printing the total string after adding the string
    front_back=""   # after printing clearing the string
    front_back=total_str
    if Start_char==122:
        Start_char=96
    Start_char+=1  # incrementing the number +1 so i can print next next characters
    