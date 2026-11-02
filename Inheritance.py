class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    def display_info(self):
        print(f"Employee name: {self.name}, Id: {self.id}")
        
# agar kabhi class ka name hange karna hai to aise karnge

class Staff(Employee):
    def show_department(self):
        print("These are the members of teaching and development department")
    
    # def __init__(self, name, id, department):
    #     super().__init__(name, id)
    #     self.department = department
        
    # def display_info(self):
    #     super().display_info()
    #     print(f"Department: {self.department}")
        
# e1 = Employee("Radhika Jain", 12345)
# e1.display_info()
# e2 = Employee("Naman Jain", 54321)
# e2.display_info()

e1 = Staff("Radhika Jain", 12345)
e1.display_info()
e2 = Staff("Naman Jain", 54321)
e2.display_info()
e2.show_department()

# s1 = Staff("Alice Smith", 67890, "HR")
# s1.display_info()
# s2 = Staff("Bob Johnson", 98765, "Finance")
# s2.display_info()