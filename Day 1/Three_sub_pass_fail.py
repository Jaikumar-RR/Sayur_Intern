# Problem #3
# you have a list of student names. you have one list each for their marks in CS, Math and English. 
# hard code the values. no need to get it as input
# Pass mark is 50.
# Grade A is, mark 90 or above
# Grade B , 80 or above
# Fail is < 50
# Print the name of the students who got A in all subjects or atleast one A and the rest B.
# Try to use only one if statement.
# List of student names
students = ["Jai", "Hari", "vasu", "David", "kabil"]

# Corresponding lists of their marks in CS, Math and English
cs_marks = [95, 85, 60, 49, 91]
math_marks = [92, 88, 80, 51, 90]
english_marks = [91, 82, 70, 50, 89]
passed_mark = 50
# Print the name of the students who got A in all subjects or at least one A and the rest B
print("Students who got A in all subjects or at least one A and the rest B:")
for i in range(len(students)):
    marks = [cs_marks[i], math_marks[i], english_marks[i]]
    if min(marks) >= 80 and max(marks) >= 90:
        print(students[i])
print("Students who got Fail in atleast one subject")
for i in range(len(students)):
    marks = [cs_marks[i], math_marks[i], english_marks[i]]
    if passed_mark > min(marks):
        print(students[i]) 