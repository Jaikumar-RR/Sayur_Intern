# problem #4
# write a program to find if two strings are same.
# two string are considered same if both strings have same letters in same order, but from different starting point
# eg abcd is same as bcda (a is moved to the right)
# abcd is same as cdab 
# abcd is  not same as cdba

# 123456 = 456123
# 123456 not = 412356
# hint - 
# there are many simple answers. you can try with slice function



String_one = input("Enter word one : ")   # asking user to give String 1
String_two = input("Enter the word two : ")   # asking user to give String 2

if(len(String_one)!=len(String_two)):   # if both String has different length we can't find the output
    print(f"Both Strings length are not same. String 1 length {len(String_one)} and String 2 length is {len(String_two)}")
    print(exit(0))  # exiting from the program

for i in range(1,len(String_one)+1):    # This for loop is to traverse the String 1
    tempStr=String_one[i:] + String_one[:i]    # each time slicing the string and store it in temp String 
    if(tempStr == String_two):  # checking the sliced String is same as String 2
        print(f"Both Strings are same at {i+1}th time") # if the Strings are same then it is the output
        break   # Then don't need to traverse the String to exiting from the loop
else:
    print(f"Both String has different characters. String 1 : {String_one} and String 2 : {String_two}")
# String_one = input("Enter word one : ")   # asking user to give String 1
# String_two = input("Enter the word two (eg: STR 1:abcde , STR 2: bcdea) : ")   # asking user to give String 2

# if(len(String_one)!=len(String_two)):   # if both String has different length we can't find the output
#     print(f"Both Strings length are not same. String 1 length {len(String_one)} and String 2 length is {len(String_two)}")
#     print(exit(0))  # exiting from the program

# for i in range(1,len(String_one)+1):    # This for loop is to traverse the String 1
#     tempStr=String_one.slice(i) + String_one.slice(0, i)    # each time slicing the string and store it in temp String 
#     if(tempStr == String_two):  # checking the sliced String is same as String 2
#         print(f"Both Strings are same at {i+1}th time") # if the Strings are same then it is the output
#         break   # Then don't need to traverse the String to exiting from the loop
# else:
#     print(f"Both String has different characters. String 1 : {String_one} and String 2 : {String_two}")
# def are_strings_same(str1, str2):
#     if len(str1) != len(str2):
#         return False

#     return str2 in str1 + str1

# # Taking user input
# string1 = input("Enter the first string: ")
# string2 = input("Enter the second string: ")

# # Checking if strings are the same when rotated
# result = are_strings_same(string1, string2)
# if result:
#     print(f"The strings '{string1}' and '{string2}' are the same when rotated.")
# else:
#     print(f"The strings '{string1}' and '{string2}' are not the same when rotated.")
