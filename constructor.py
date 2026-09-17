# __init__ Function
#All classes have a function called _init_(), which is always exectued when the object is being initiated.


class Student:
    #Constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database..")

s1 = Student("karan", 97)
print(s1.name, s1.marks)

s2 = Student("arjun", 87)
print(s2.name, s2.marks)