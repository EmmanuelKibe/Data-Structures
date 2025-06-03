#initialize an empty dictionary to store students and their marks
student_list = {}
student1 = {'John' : [90, 45, 78]}
student_list.update(student1)

# Function to input student name and grades
def student_input():
    student_name = input('Enter the name of the student: ')
    grades = input('Enter a list of the marks separated by a comma: ')
    
    grades = [int(grade.strip()) for grade in grades.split(',')]
    
    student_list [student_name] = grades

# Function to calculate the average grade of a student
def average_grades():
    student_name = input('Enter the name of the student to calculate average grade: ')
    if student_name in student_list:
        grades = student_list[student_name]
        average = sum(grades) / len(grades)
        print(f'The average grade for {student_name} is {average:.2f}') 
    else:
        print('Student not found.' )    

def highest_grade():
    student_name = input('Enter the name of the student to find the highest grade: ')
    if student_name in student_list:
        grades = student_list[student_name]
        highest = max(grades)
        print(f"{student_name}'s highest grade is {highest}")
    else:
        print('Student not found.')

def lowest_grade():
    student_name = input('Enter the name of the student to find the lowest grade: ')
    if student_name in student_list:
        grades = student_list[student_name]
        lowest = min(grades)
        print(f"{student_name}'s lowest grade is {lowest}")
    else:
        print('Student not found.')




