class Student:

    # 1. Constructor
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    # 2. Getter using decorator
    @property
    def marks(self):
        return self.__marks

    # 3. Setter using decorator
    @marks.setter
    def marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
        else:
            print("Marks must be between 0 and 100!")

    # 4. Method to display student details
    def display(self):
        print("\n--- Student Details ---")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")


# 5. Creating an object
student1 = Student("Naman", 85)

# Display student details
student1.display()

# Update marks using setter
student1.marks = 95

# Read updated marks using getter
print("\nUpdated Marks:", student1.marks)

# Try invalid marks
student1.marks = 150