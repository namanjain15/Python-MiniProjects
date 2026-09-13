# -------------------------------
# Student Result Management System
# -------------------------------

import math

# Variables + Data Types
student_name = "Naman"
roll_no = 101
marks = [85, 78, 92, 88, 76]       # List
subjects = {"Python", "DBMS", "AI", "Java", "Math"}  # Set
is_student = True                  # Boolean

# Typecasting
roll_no = int(roll_no)
average = float(sum(marks) / len(marks))

# Function to calculate total marks
def calculate_total(marks):
    return sum(marks)

# Function to calculate percentage
def calculate_percentage(marks):
    total = calculate_total(marks)
    return (total / (len(marks) * 100)) * 100

# Function to check result
def check_result(percentage):
    if percentage >= 90:
        return "Excellent"
    elif percentage >= 75:
        return "Very Good"
    elif percentage >= 60:
        return "Good"
    elif percentage >= 40:
        return "Pass"
    else:
        return "Fail"


# Calculate results
total = calculate_total(marks)
percentage = calculate_percentage(marks)
result = check_result(percentage)

# Using math module
rounded_percentage = math.ceil(percentage)

# For loop
print("\nSubject-wise Marks:")
for i in range(len(marks)):
    print(f"{list(subjects)[i]}: {marks[i]}")

# F-string
print("\n----- Student Result -----")
print(f"Student Name : {student_name}")
print(f"Roll Number  : {roll_no}")
print(f"Total Marks  : {total}/500")
print(f"Percentage   : {percentage:.2f}%")
print(f"Result       : {result}")
print(f"Rounded %    : {rounded_percentage}%")
print(f"Student      : {is_student}")