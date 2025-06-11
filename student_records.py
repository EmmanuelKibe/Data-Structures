#Store student records as a list of tuples
students = [("Alice", "Bob", "Charlie"), (20, 21, 22), ("Math", "Science", "History")]

def display_student_records():
    print("Student Names:", students[0])
    print("Ages:", students[1])
    print("Subjects:", students[2])

def search_by_name():
    name = input("Enter the student's name to search: ")
    if name in students[0]:
        index = students[0].index(name)
        print(f"Found {name}: Age - {students[1][index]}, Subject - {students[2][index]}")
    else:
        print(f"{name} not found in records.")

search_by_name()