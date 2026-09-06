def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

num_subjects = int(input("Enter number of subjects: "))
marks = []

for i in range(num_subjects):
    score = float(input(f"Enter marks for subject {i + 1} (out of 100): "))
    marks.append(score)

total_marks = sum(marks)
max_possible = num_subjects * 100
percentage = (total_marks / max_possible) * 100
grade = calculate_grade(percentage)

print("\n--- Result ---")
print(f"Total Marks: {total_marks:.2f} / {max_possible}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")