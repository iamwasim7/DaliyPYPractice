#Conceptual implementations in Python
#Private attribute & methods to be used only within the class and are not accessible from outside the class.

class Person:
    __name = "anonymous" # __before attribute or object makes it private & only internal func can acess the private 

    def __hello(self):
        print("hello person!")

    def welcome(self):
        self.__hello()


p1 = Person()
print(p1.welcome())