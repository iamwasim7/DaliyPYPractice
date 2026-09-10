#List are created like this-
IPLTEAMS = ["KKR", "SRH", "MI", "RCB", "CSK", "RR", "DC"]
print(IPLTEAMS)

#List Items
#List items are ordered, changeable, and allow duplicate values.
#List items are indexed, the first item has index [0], the second item has index [1] etc.

#Ordered
#When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
#If you add new items to a list, the new items will be placed at the end of the list.

#Changeable
#The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

#Allow Duplicates
#Since lists are indexed, lists can have items with the same value:
list2 = ["apple", "banana", "watermelon", "apple", "banana", "Cherry"]
print(list2)

#List Length
#To determine how many items a list has, use the len() function:

list3 = ["apple", "banana", "watermelon"]
print(len(list3))

#List Items - Data Types
#List items can be of any data type:

listInt = [56, 49, 1, 7, 33, 55, 77]
listString = ["India", "Austrila", "England"]
listBoolean = [True, False, True]

#A list can contain different data types:

list4 = ["Wasim", "Bsc.IT", 39, "TY.IT", True]

#Access Items
#List items are indexed and you can access them by referring to the index number:

print(list4[0:3])