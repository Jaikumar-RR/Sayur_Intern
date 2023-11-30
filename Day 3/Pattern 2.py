# Problem 1
# Print the following pattern
#      1
#     1 1
#    1 2 1
#   1 3 3 1
#  1 4 6 4 1

# Observe how the nunmbers in the triangle are calculated. 
# Do it in two steps. Work on the generating the numbers first in right angle triangle


def print_pascals_triangle(rows):
    for i in range(rows):
        print(" " * (rows - i), end="")
        C = 1
        for j in range(i + 1):
            print(C, end=" ")
            C = C * (i - j) // (j + 1)
        print()

# Call the function
Number_of_rows = int(input("Enter Number of rows : "))
print_pascals_triangle(Number_of_rows)

