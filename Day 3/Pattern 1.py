# Problem 1

# Observe how the nunmbers in the triangle are calculated. 
# Do it in two steps. Work on the generating the numbers first in right angle triangle
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1

# And then work on the final output using proper indendation

def print_pascals_triangle(rows):
    for line in range(1, rows + 1):
        C = 1  # used to represent C(line, i)
        for index in range(1, line + 1):
            # The first value in a line is always 1
            print(C, end = " ")
            # Using Binomial Coefficient formula
            C = C * (line - index) // index
        print()

# Call the function
Number_of_rows = int(input("Enter Number of rows : "))
print_pascals_triangle(Number_of_rows)
