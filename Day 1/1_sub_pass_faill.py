# In your college Python is taught in 3 different departments by the same professor. 
# For each dept, get the no of students stutying Python and their marks in the final exam 
# Get the input as comma seperated string

# Find the top 3 marks in each class
# Find the top 3 marks if all classes are combined.
# Find the avg mark of students with passing mark in each class and the classes combined.
# Find which class has the best average mark and least number of failed students.
# List of student names
students = ["Jai", "Hari", "vasu", "David", "kabil"]

# Corresponding list of their marks in CS
marks = [55, 45, 60, 49, 51]

# Pass mark
pass_mark = 50

# List to store students with pass marks
passed_students = []

# List to store students who failed
failed_students = []

# Iterate over students and their corresponding marks
for i in range(len(students)):
    if marks[i] >= pass_mark:
        # If the student has passed, add them to the passed_students list
        passed_students.append(f"{students[i]}:{marks[i]}")
    else:
        # If the student has failed, add them to the failed_students list
        failed_students.append(f"{students[i]}:{marks[i]}")

# Print the list of students who passed
print("Passed Students List:")
for student in passed_students:
    print(student)
print("------------------------")
# Print the list of students who failed
print("Failed Student List:")
for student in failed_students:
    print(student)
print("------------------------")
# Print the number of students who failed
print(f"Number of Passed Students: {len(passed_students)}")
print(f"Number of Failed Students: {len(failed_students)}")
