# problem #5
# In your college Python is taught in 3 different departments by the same professor. 
# For each dept, get the no of students stutying Python and their marks in the final exam 
# Get the input as comma seperated string
# Find the top 3 marks in each class
# Find the top 3 marks if all classes are combined.
# Find the avg mark of students with passing mark in each class and the classes combined.
# Find which class has the best average mark and least number of failed students.
#define a function with passing an parameter
def Python_Mark_Caluclation(data):
    # Initialize empty variables to store values
    top_3_marks = {}
    avg_marks = {}
    failed_students = {}
    combined_marks = []#Intialize empty list variable
    passing_marks = 50  # Assuming 50 as the passing mark

    # Process students data for each department
    for dept, students in data.items():#Using items() to seperate the key and value and store on dept,studemts
        #By using for loop to store student data on student var and get the mark seperately and store on marks
        marks = [int(student.split(':')[1]) for student in students]
        #By Using for loop to store pass marks on passed_students
        passed_students = [mark for mark in marks if mark >= passing_marks]

        # Top 3 marks in each class
        top_3_marks[dept] = sorted(marks, reverse=True)[:3]#By using Sorted() make values on decending order and get top 3 marks 

        # Average mark of students with passing mark in each class
        #Using (sum()-to add values on list and len()-length of the list) for calculation 
        avg_marks[dept] = sum(marks) / len(marks) 

        # Number of failed students in each class
        failed_students[dept] = len([mark for mark in marks if mark < passing_marks])

        # Combine all marks
        combined_marks.extend(marks)

    # Top 3 marks if all classes are combined
    combined_top_3 = sorted(combined_marks, reverse=True)[:3]#same as above make sort

    # Average mark of students with passing mark in all classes combined
    combined_avg = sum(combined_marks) / len(combined_marks)

    # Class with the best average mark and least number of failed students
    best_avg_class = max(avg_marks, key=avg_marks.get)#using max() to get max value on dict

    min_failures = min(failed_students.values())
    least_failures_class = [dept for dept, failures in failed_students.items() if failures == min_failures]
    #printing all output we need
    print("Top 3 Marks :",top_3_marks)
    print("Avg_mark :",avg_marks)
    print("Failed_Student :",failed_students)
    print("Combined Top 3 Marks :",combined_top_3)
    print("Combined Top 3 Avg :",combined_avg)
    print("Best_avg_class : ",best_avg_class)
    print("Least Failure Class :",least_failures_class)



# Test the function
dept_stud_data = {
    'Dept1': ['Student1:25', 'Student2:20', 'Student3:38', 'Student4:42', 'Student5:88'],
    'Dept2': ['Student1:80', 'Student2:85', 'Student3:99', 'Student4:26', 'Student5:84'],
    'Dept3': ['Student1:70', 'Student2:75', 'Student3:100', 'Student4:76', 'Student5:74']
}

Python_Mark_Caluclation(dept_stud_data)
