#Python Conditions and If statements
#Python supports the usual logical conditions from mathematics:

#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b
#These conditions can be used in several ways, most commonly in "if statements" and loops.
#An "if statement" is written by using the if keyword.

#Simple If Statement :
a = 5
b = 10

if b > a:
    print("b is bigger than a")
    
#How If Statements Work
#The if statement evaluates a condition (an expression that results in True or False). If the condition is true, the code block inside the if statement is executed. If the condition is false, the code block is skipped.

#The Elif Keyword
#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
#The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.

if a > b:
    print("A is bigger than B")
elif a>b:
    print("B is bigger than A")
    
#The Else Keyword
#The else keyword catches anything which isn't caught by the preceding conditions.
#The else statement is executed when the if condition (and any elif conditions) evaluate to False.

c = 300
d = 100

if c == d:
    print("C is equal to D")
elif c > d:
    print("C is bigger than D")
else:
    print("C is smaller than D")