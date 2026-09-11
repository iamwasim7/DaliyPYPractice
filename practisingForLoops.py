#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
#The for loop does not require an indexing variable to set beforehand.

#Simple For loop prg:
fruits = ["Apple", "Banana", "Watermelon", "Kiwi"]
for i in fruits:
    print(i)


#The break Statement
#With the break statement we can stop the loop before it has looped through all the items:

for i in fruits:
    print(i)
    if i == "Banana":
        break


