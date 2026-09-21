#Methods are functions that belong to objects.
#class stores two things - 
# - data (attributes)
# - methods (functions)

class Student:
    college_name = "DTSS College of Commerce & Science"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self): #Method to get name
        print("Welcome Student", self.name)

    def get_marks(self): #Method to get marks
        return self.marks

s1 = Student("karan", 97)
s1.welcome()
print(s1.get_marks())
