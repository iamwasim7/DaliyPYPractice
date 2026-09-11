#Set
#Sets are used to store multiple items in a single variable.
#Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
#A set is a collection which is unordered, unchangeable*, and unindexed.

#This is how we make Set in py:
mySet = {"BMW", "Porsche", "Toyota"}
print(mySet)

#Duplicates Not Allowed
#Sets cannot have two items with the same value.

mySet2 = {"A", "B", "C", "D", "A", "C", "D"}
print(mySet2)

#Access Items
#You cannot access items in a set by referring to an index or a key.
#But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

for i in mySet:
    print(i)
    
#Change Items
#Once a set is created, you cannot change its items, but you can add new items.

#Add Items
#To add one item to a set use the add() method.

mySet.add("Tesla")
print(mySet)