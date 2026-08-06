print("=" * 50)
print("          PREPTRACK APPLICATION")
print("=" * 50)
print()
while True:
    student_name = input("Enter student name: ")

    if student_name != "":
        break
    else:
        print("Student name cannot be empty.")

print("Student Name:", student_name)
print()