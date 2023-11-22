# Problem #1
# Print the following pattern
# 1
# 212
# 32123
# 4321234
# 543212345
# Get user input for how far to go (up to 0)

Num_of_rows = int(input("Enter Number of Rows you wants : "))
prev_num = ""
for index in range(1,Num_of_rows+1):
    result = str(index)+prev_num
    print(result)
    prev_num = result + str(index + 1)
